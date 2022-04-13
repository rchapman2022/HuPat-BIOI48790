-- Data Definition for the HuPat Database

-- Creates the Taxonomy Table to represent an NCBI Taxonomy entry associated with an organism. 
-- The table contains the following attributes:
---- taxID (Primary Key) - NCBI’s identifier code for the taxonomy
---- ncbi_tax_link - A link to the NCBI page for the taxonomy.
CREATE TABLE Taxonomy (
    taxID VARCHAR(10) NOT NULL PRIMARY KEY,
    ncbi_tax_link VARCHAR(200) NOT NULL
);

-- Creates the Organism Table to represent an organism. The table contains the following
-- attributes:
---- Organism ID - An automatically generated identification number for the organism. 
----               This value is arbitrary and is stored primarily for table reference 
----               and future expansion.
---- Linkeage - The taxonomic lineage of the given organism. A list of taxonomic levels 
----            from kingdom to phylum, separated by semi-colon. 
---- organism_rank - The current taxonomic rank of the organism. Will be species in most cases.
---- organism_name - The scientific name for the organism.
---- taxID (Foreign Key references Taxonomy(taxID) - The NCBI taxonomy ID for the organism.
CREATE TABLE Organism (
    organismID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    lineage VARCHAR(500) NOT NULL,
    organism_rank VARCHAR(20) NOT NULL,
    organism_name VARCHAR(50) NOT NULL,
    taxID VARCHAR(10) NOT NULL REFERENCES Taxonomy(taxID)
);

-- Creates the RefSeqEntry Table to represent a RefSeq genome assembly for an organism. The
-- table contains the following attributes:
---- refSeq_accession (Primary Key) - NCBI’s RefSeq database accession number for the assembly.
---- ncbi_refseq_link - A link to the NCBI RefSeq entry for the assembly.
---- assembly_link - A link to the NCBI FTP site to download the assembly.
---- organismID (Foreign Key references Organism(organismID)) - The ID for the organism associated 
----                                                            with the assembly.
CREATE TABLE RefSeqEntry (
    refSeq_accession VARCHAR(20) NOT NULL PRIMARY KEY,
    ncbi_refseq_link VARCHAR(200) NOT NULL,
    assembly_link VARCHAR(200) NOT NULL,
    organismID INT NOT NULL REFERENCES Organism(organismID)
);

-- Creates the PubMedEntries Table to represent the most recent PubMed article associated with
-- an organism. The table contains the following attributes:
---- pubmedID (Primary Key) - NCBI’s identifier for the PubMed article.
---- article_title - The title of the PubMed article.
---- article_link - A link to the NCBI PubMed site to access the article.
CREATE TABLE PubMedEntries (
    pubmedID VARCHAR(20) NOT NULL PRIMARY KEY,
    article_title VARCHAR(500) NOT NULL,
    article_link VARCHAR(200) NOT NULL
);

-- Creates the OrganismPubMedLink Table which connects an organism to a pubmed article. This allows
-- multiple organisms to be associated with the same pubmed article. The table contains the following
-- attributes:
---- organismID (Foreign Key references Organism(organismID)) - The ID of the organism to be associated with the pubmed article.
---- pubmedID (Foreign Key references PubMedEntry(pubmedID)) - NCBI’s identifier for the PubMed article.
----
---- Primary Key: (organismID, pubmedID)
CREATE TABLE OrganismPubMedLink (
    organismID INT NOT NULL REFERENCES Organism(organismID),
    pubmedID VARCHAR(20) NOT NULL REFERENCES PubMedEntries(pubmedID),

    CONSTRAINT PK_OrganismsPubMedLink PRIMARY KEY (organismID,pubmedID)
);

