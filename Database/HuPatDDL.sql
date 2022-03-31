-- Data Definition for HuPat

CREATE TABLE Taxonomy (
    taxID VARCHAR(20) NOT NULL PRIMARY KEY,
    ncbi_tax_link VARCHAR(200) NOT NULL
);

--Creates the Organism Table
---- Organism ID - A unique identifier that represents an Organism
---- Linkeage - Taxonomic lineage of the Organism
---- organism_rank - Current Taxonomic rank of the organism
---- organism_name - The name of the organism
---- taxID - A unique taxonomic ID of the organism
CREATE TABLE Organism (
    organismID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    lineage VARCHAR(100) NOT NULL,
    organism_rank VARCHAR(20) NOT NULL,
    organism_name VARCHAR(50) NOT NULL,
    taxID VARCHAR(20) NOT NULL REFERENCES Taxonomy(taxID),
);


CREATE TABLE RefSeqEntry (
    refSeq_accession VARCHAR(20) NOT NULL PRIMARY KEY,
    ncbi_refseq_link VARCHAR(100) NOT NULL,
    assembly_link VARCHAR(100) NOT NULL,
    organismID INT NOT NULL REFERENCES Organism(organismID),
);

CREATE TABLE PubMedEntries (
    pubmedID VARCHAR(20) NOT NULL PRIMARY KEY,
    article_link VARCHAR(200) NOT NULL
);

CREATE TABLE OrganismPubMedLink (
    organismID INT NOT NULL REFERENCES Organism(organismID),
    pubmedID VARCHAR(20) NOT NULL REFERENCES PubMedEntries(pubmedID),

    CONSTRAINT PK_OrganismsPubMedLink PRIMARY KEY (organismID,pubmedID),
);

