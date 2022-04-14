<?php

/* SearchOrganism.php - The Search Organism Script acts as a back-end which retrieves the organism name
   submitted by the user on the front end, uses it to query the HuPat MySQL database, 
   and returns the retrieved data in JSON format to the front-end. */

/* Define variables containing credentials for database connection */
$server="localhost";
$username="rchapman";
$password="";
$database="rchapman";


/* Connect to MySQL database using defined credentials
* throws an error if connection is not successful */
$connect = mysqli_connect($server,$username,"",$database);

if ($connect->connect_error){
	echo "Something went wrong connecting";
}

/* Sets the $_POST variable to retrieve from php input */
$_POST = json_decode(file_get_contents('php://input'), true);

/* Grabs the organism name from the post */
$orgname = $_POST['OrgName'];

/* Creates the SQL query to grab relevant data for this organism */
$query = "SELECT lineage, organism_rank, organism_name, t.taxID, ncbi_tax_link, refSeq_accession, 
            ncbi_refseq_link, assembly_link, article_title, article_link FROM Organism AS o JOIN Taxonomy AS t 
            ON o.taxID = t.taxID LEFT JOIN RefSeqEntry AS r ON o.organismID = r.organismID JOIN OrganismPubMedLink AS opl 
            ON o.organismID = opl.organismID JOIN PubMedEntries AS p ON p.pubmedID = opl.pubmedID WHERE organism_name = '$orgname';";

/* Uses the mysql connector to perform this query on the database */
$result = mysqli_query($connect, $query);

/* Checks to ensure that the query has been completed */
if ($result = mysqli_query($connect, $query)) {
    
    /* Grabs the query output (Should only be 1 set of data per organism) */
    $row = mysqli_fetch_row($result);
    
    /* If the data is empty, then it returns an error status */
    if ($row['0'] == "") {
	    echo '{"status":"error"}';
    }
    else {

        /* Creates an array called data and ties the query results to their
        * respective variables names. PHP allows easy conversion of arrays
        * into JSON data. */
        $data = array('status' => "success", 'lineage' => "$row[0]", 'rank' => "$row[1]", 'orgName' => "$row[2]", 'taxID' => "$row[3]", 
        'taxLink' => "$row[4]", 'assembly' => "$row[5]", 'refSeqLink' => "$row[6]", 'downloadLink' => "$row[7]",
        'title' => "$row[8]", 'articleLink' => "$row[9]");
    
        /* Retruns the data as a JSON object */
        echo json_encode($data, JSON_FORCE_OBJECT);
    }
}
else {
    /* If the query was performed incorrectly, also return
    * and error status */
    echo '{"status":"error"}';
}

/* Close the MySQL connection */
mysqli_close($connect);
?>
