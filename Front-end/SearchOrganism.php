<?php

/*Connection variables at top
* Makes it easy to change if needed*/
$server="localhost";
$username="rchapman";
$password="";
$database="rchapman";


/*Connect to my database
* and throw errors if its unable to connect.
* Greets the web user if it is able to connect.*/
$connect = mysqli_connect($server,$username,"",$database);

if ($connect->connect_error){
	echo "Something went wrong connecting";
}

$_POST = json_decode(file_get_contents('php://input'), true);

$orgname = $_POST['OrgName'];

/*$arr = array('seen' => "$orgname");
echo json_encode($arr, JSON_FORCE_OBJECT);*/

$query = "SELECT lineage, organism_rank, organism_name, t.taxID, ncbi_tax_link, refSeq_accession, 
            ncbi_refseq_link, assembly_link, article_title, article_link FROM Organism AS o JOIN Taxonomy AS t 
            ON o.taxID = t.taxID JOIN RefSeqEntry AS r ON o.organismID = r.organismID JOIN OrganismPubMedLink AS opl 
            ON o.organismID = opl.organismID JOIN PubMedEntries AS p ON p.pubmedID = opl.pubmedID WHERE organism_name = '$orgname';";

#echo $query;

$result = mysqli_query($connect, $query);

#echo "Ran query";

if ($result = mysqli_query($connect, $query)) {

    #echo "Hit query success";

    $row = mysqli_fetch_row($result);

    #echo $row;

    $data = array('status' => "success", 'lineage' => "$row[0]", 'rank' => "$row[1]", 'orgName' => "$row[2]", 'taxID' => "$row[3]", 
    'taxLink' => "$row[4]", 'assembly' => "$row[5]", 'refSeqLink' => "$row[6]", 'downloadLink' => "$row[7]",
    'title' => "$row[8]", 'articleLink' => "$row[9]");
    
    echo json_encode($data, JSON_FORCE_OBJECT);
}
else {
    echo '{"status":"error"}';
}
mysqli_close($connect);
?>
