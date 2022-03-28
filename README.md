# HuPat - Human Pathogen Sequence Repository
Repository for BIOI4870 undergraduate course project

## Site Availability
HuPat can be accessed at http://odin.unomaha.edu/~rchapman/HuPat/home.html

## Purpose
The purpose of the Human Pathogen Sequence Repository (HuPat) is to compile genetic sequence data from human pathogens for search, retrieval, and analysis. Without a consolidated and concise repository for this data, any in silico procedure is inherently disadvantaged, as additional data manipulation and retrieval will be required. In many cases, these additional measures required bioinformatics experience, which is not universal amongst biomedical researchers. The creation of HuPat should lead to both consolidation human pathogen sequencing as well as increase the accessibility of such analyses to a wider array of scientists.

## Project Goals
Given the limited timeframe (1 semester) and the size constraints of the development environment, HuPat’s database will house taxonomic data, truncated genomic data, and external references to NCBI for 2 different human pathogens. The represented pathogens will be manually selected based on relative disease burden as suggested by literature. The process of downloading and truncating the data will be automated using python and using Biopython’s Bio.Entrez functionality. 

The taxonomic data for each organism will be downloaded from NCBI’s Taxonomy database and will include:
-	TaxonomyID
-	Rank
-	Lineage
-	NCBI Organism Link
-	NCBI Genome Link
-	NCBI Taxonomy Link

The genomic data will be truncated to ~100MB per organism to ensure that the data fits within the size constraints set by Odin and stored in FASTA format.

## File Structure

*To be added*

## Changelog

03/16/2022 - Created Repository and added intial information to README.md
