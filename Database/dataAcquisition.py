from Bio import Entrez
import MySQLdb

NCBI_Tax_Link_prefix = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id="
NCBI_RefSeq_Link_prefix = "https://www.ncbi.nlm.nih.gov/assembly/"
NCBI_PubMed_Link_prefix = "https://pubmed.ncbi.nlm.nih.gov/"


# The purpose of this script is to automate the process of data collection and 
# entry into the HuPat database. The script will be run daily via a cron job
# to ensure that records are update.
#
# The script utilizes the Biopython Entrez package to query the NCBI Taxonomy,
# RefSeq, and PubMed Databases. Additionally, the script utilizes the python
# MySQL package to modify the database. 

def main():
    
    # Create MySQL connection and cursor
    cnx = MySQLdb.connect(user="rchapman", password='', host='localhost', db='rchapman', use_unicode=True, charset="utf8")
    cursor = cnx.cursor()

    # Read in file containing list of organism taxonomic classifications
    inFile = open("./OrganismsToSearch.txt", 'r')

    # Enter email for Biopython Entrez functionality (required)
    Entrez.email = "rchapman@unomaha.edu"

    # Clear MySQL Tables
    cursor.execute("DELETE FROM Organism; DELETE FROM RefSeqEntry; DELETE FROM Taxonomy; \
        DELETE FROM PubMedEntries; DELETE FROM OrganismPubMedLink;")

    # Loop over organisms provided in file and grab the necessary data using Entrez
    for org in inFile:

        # Searches the Taxonomy database using the organism to identify
        # entry IDs
        initialTaxSearch = Entrez.esearch(db="taxonomy", term=org)
        initialTaxRec = Entrez.read(initialTaxSearch)

        # Utilizes the entry ID found above to retrieve the record
        taxHandle = Entrez.efetch(db="taxonomy", id = initialTaxRec["IdList"][0])
        taxRec = Entrez.read(taxHandle)

        # Grab the TaxonomyID, Scientific Name, Rank, and Lineage from the
        # NCBI Taxonomy Entry
        taxID = taxRec[0]['TaxId']
        OrgName = taxRec[0]['ScientificName']
        rank = taxRec[0]['Rank']
        lineage = taxRec[0]['Lineage']

        # Close Entrez Handles
        initialTaxSearch.close()
        taxHandle.close()
        
        # Creates and executes an insert statemtn for the Taxonomy table
        insertTax = "INSERT INTO Taxonomy (taxID, ncbi_tax_link) VALUES ('{0}', '{1}');".format(taxID, NCBI_Tax_Link_prefix + taxID)
        cursor.execute(insertTax)

        # Creates an executes an insert statement for the Organism table
        insertOrg = "INSERT INTO Organism (lineage, organism_rank, organism_name, taxID) VALUES ('{0}', '{1}', '{2}', '{3}');".format(lineage, rank, OrgName, taxID)
        cursor.execute(insertOrg)


        # The OrganismID attribute is an autoincrementing key generated by MySQL.
        # Thus, we need to retrieve it to enter in subsequent tables
        grabOrgID = "SELECT organismID FROM Organism WHERE organism_name = '{0}';".format(OrgName)
        cursor.execute(grabOrgID)
        orgId = cursor.fetchone()[0]

        # Searches the NCBI Assembly Database for genome assemblies filtered for the organism
        # and for only reference genomes
        initialRefSeqSearch = Entrez.esearch(db="assembly", term="{0}[Organism] AND \"reference genome\"[filter]".format(org))
        initialRefSeqRec = Entrez.read(initialRefSeqSearch)

        refSeqRec = ''
        refSeqHandle = ''
        # Some organisms have a reference genome, while others do not. 
        # If there is not a reference genome, search the database again
        # for a representative genome.
        if (len(initialRefSeqRec["IdList"]) == 0):

            # Searches the assembly database for the given organism and it's representative genome
            initialRefSeqSearch = Entrez.esearch(db="assembly", term="{0}[Organism] AND \"representative genome\"[filter]".format(org))
            initialRefSeqRec = Entrez.read(initialRefSeqSearch)

        # Still, some organisms will not have a representative genome. If
        # either search came back positive, the ID retrieved will be used to
        # grab the full entry. If not, the RefSeq entry will be skipped. 
        if (len(initialRefSeqRec["IdList"]) != 0):
            # Uses the NCBI Assembly entry ID to grab the record.
            refSeqHandle = Entrez.esummary(db="assembly", id = initialRefSeqRec["IdList"][0], report="full")
            refSeqRec = Entrez.read(refSeqHandle)

            # Grabs the RefSeq Genome Accession Number and RefSeqFTP Link
            # Also creates a link to the RefSeq entry using the accession number
            # and the general NCBI Link format
            refSeqAcc = refSeqRec['DocumentSummarySet']['DocumentSummary'][0]["Synonym"]["RefSeq"]
            refSeqFTP = refSeqRec['DocumentSummarySet']['DocumentSummary'][0]["FtpPath_RefSeq"]
            refSeqLink = NCBI_RefSeq_Link_prefix + refSeqAcc + "/"

            # Creates and executes an insert statement for the RefSeqEntry table
            insertRefSeq = "INSERT INTO RefSeqEntry (refSeq_accession, ncbi_refseq_link, assembly_link, organismID) VALUES ('{0}', '{1}', '{2}', {3})".format(refSeqAcc, refSeqLink, refSeqFTP, orgId)
            cursor.execute(insertRefSeq)

            # Close Entrez Handle
            refSeqHandle.close()

        # Close Intital Search Entrez Handle
        initialRefSeqSearch.close()
        

        # Searches the NCBI PubMed Database for articles references in the organism
        # Results are sorted by date, to grab the most recent publication
        initialPubMedSearch = Entrez.esearch(db="pubmed", term="{0}".format(org), sort ="pub date")
        initialPubMedRec = Entrez.read(initialPubMedSearch)
        

        # Use the NCBI PubMed ID to grab the record
        pubMedHandle = Entrez.esummary(db="pubmed", id=initialPubMedRec["IdList"][0])
        pubMedRec = Entrez.read(pubMedHandle)

        # Grab the Publication Title, NCBI PubMed ID, and create a link given the NCBI prefix
        pubMedTitle = pubMedRec[0]['Title']
        pubMedID = pubMedRec[0]['Id']
        pubMedLink = NCBI_PubMed_Link_prefix + pubMedID + "/" 

        # Close Entrez Handles
        initialPubMedSearch.close()
        pubMedHandle.close()

        # Creates and executes an insert statment for the PubMedEntry table
        insertPubMed = "INSERT INTO PubMedEntries (pubmedID, article_title, article_link) VALUES ('{0}', '{1}', '{2}');".format(pubMedID, pubMedTitle, pubMedLink)
        cursor.execute(insertPubMed)

        # Creates and executes an insert statement for the OrganismPubMedLink table
        insertPubOrgLink = "INSERT INTO OrganismPubMedLink (organismID, pubmedID) VALUES ('{0}', '{1}');".format(orgId, pubMedID)
        cursor.execute(insertPubOrgLink)

    # Close the MySQL cursor, mysql Connection and the input file.
    cursor.close()
    cnx.commit()
    cnx.close()
    inFile.close()


if __name__ == "__main__":
    main()
