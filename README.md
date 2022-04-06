# HuPat - Human Pathogen Sequence Repository
![HuPat Logo]https://github.com/rchapman2022/HuPat-BIOI48790/blob/main/Front-end/HuPatLogo.JPG
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

## Database Design

### ER Diagram
![HuPat ER Diagram](https://github.com/rchapman2022/HuPat-BIOI48790/blob/main/Documentation/HuPatERDiagram.png)

## Changelog

- 03/16/2022 - Created Repository and added intial information to README.md
- 03/20/2022 - Created Intital Draft of database DDL
- 03/27/2022 - Developed the HuPat Homepage HTML
- 03/28/2022 - Continued front-end modification and began developing PHP back-end
- 03/31/2022 - Developed, tested, and completed a python script to automate data acquisition
- 04/03/2022 - Connected and finalized PHP back-end and HTML front-end integration
- 04/05/2022 - Added supporting code comments, tweaked search result posting events, modified database schema and aquisition script to be able to hold entrie without a reference genome (either a representative genome or no genome), and updated front-end to handle entries with no RefSeq assembly
