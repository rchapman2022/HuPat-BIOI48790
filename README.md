# HuPat - Human Pathogen Sequence Repository
<p align="center">
  <img src="https://github.com/rchapman2022/HuPat-BIOI48790/blob/main/Front-end/HuPatLogo.JPG">
</p>

Repository for BIOI4870 undergraduate course project

## Site Availability
HuPat can be accessed at http://odin.unomaha.edu/~rchapman/HuPat/home.html

### Organisms Present in Databse
- escherichia coli
- staphylococcus aureus
- helicobacter pylori
- toxoplasma gondii
- plasmodium falciparum
- naegleria fowleri
- candida albicans
- cryptococcus neoformans
- aspergillus fumigatus
- pseudomonas aeruginosa

### Utilization
<p align="center">
  <img style="background-color: rgb(300, 300, 300);" src="https://github.com/rchapman2022/HuPat-BIOI48790/blob/main/Documentation/EmptyHomepage.JPG">
</p>

Upon loading the site, the page will appear blank. You can scroll to read information about the page on the righthand side. To display organism data, enter an organism name from the provided list, and click submit.

<p align="center">
  <img style="background-color: rgb(300, 300, 300);" src="https://github.com/rchapman2022/HuPat-BIOI48790/blob/main/Documentation/PopulatedHomepage.JPG">
</p>


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

### Front-end Directory
| File | Description |
| --- | --- |
| home.html | An html file that encodes the user interface of the website. The formatting was created using Bootstrap5, and Javascript was used to developed to create any dynamic page functionality and connect to the php back-end. |
| HuPatLogo.JPG | A .jpg file containing the HuPat logo to be displayed on the webpage. |
| SearchOrganism.php | A php script that queries the MySQL database using the organism entered by the user. |

### Database Directory 
| File | Description |
| --- | --- |
| dataAcquisition.py | A python script that automatically queries the NCBI Taxonomy, PubMed, and Assembly databases to gather data for the database. Ideally this script could be automated via a cron job to update the database daily. The script pulls a list of organisms from th OrganismsToSearch.txt file. |
| HuPatDDL.sql | A sql script that creates the database tables in MySQL. More information on the database design can be found in the Databse Design section of this document. |
| OrganismsToSearch.txt | A simple text file that contains a list of pathogenic organisms that are used to populate the database. |
| esummary_assembly.dtd and ulist.dtd | Automatically generated files by MySQL. |

### Documentation
This section contains documentation submitted with the course project.

## Database Design

### ER Diagram
<p align="center">
  <img style="background-color: rgb(300, 300, 300);" src="https://github.com/rchapman2022/HuPat-BIOI48790/blob/main/Documentation/HuPatERDiagram.jpg">
</p>

### Data Dictionary 
The Data dictionary for HuPat can be found in the [DDL text document](https://github.com/rchapman2022/HuPat-BIOI48790/blob/main/Documentation/HuPatDDL.txt)


## Changelog

- 03/16/2022 - Created Repository and added intial information to README.md
- 03/20/2022 - Created Intital Draft of database DDL
- 03/27/2022 - Developed the HuPat Homepage HTML
- 03/28/2022 - Continued front-end modification and began developing PHP back-end
- 03/31/2022 - Developed, tested, and completed a python script to automate data acquisition
- 04/03/2022 - Connected and finalized PHP back-end and HTML front-end integration
- 04/05/2022 - Added supporting code comments, tweaked search result posting events, modified database schema and aquisition script to be able to hold entrie without a reference genome (either a representative genome or no genome), and updated front-end to handle entries with no RefSeq assembly
