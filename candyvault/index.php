<?php
error_reporting(-1);


//print_r(get_defined_functions());

//$_POST['password'] = 'hunter2';
$password = $_POST['password'];

$pw = array("hunter2", "hello_iver", "Sommar2020", "S3CuR3P4ssw000rd", "C4nDyISGREAT");
foreach($pw as $p){
    if (md5($p) == md5($password)){
        echo "Banned";
        die();
    }
}





$check = keyvault_check($_POST['password']);
if ($check == true){
    echo "Valid";
} else {
    echo "Invalid";
}