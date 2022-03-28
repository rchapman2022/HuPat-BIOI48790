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

$orgname = $_POST['OrgName'];

$query = "SELECT * FROM Organism WHERE orgName = \'$orgname\';"


echo json_encode($results);

?>