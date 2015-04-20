<?php

$white_list = array('.', '..', 'post.php', 'check.php');

$d = dir(".");

$clean = $_GET['clean'] ? true : false;


while (false !== ($entry = $d->read())) {
    if(!in_array($entry, $white_list)){
        if($clean){
            unlink($entry);
        }else{
            echo "http://attacker.com/$entry";
            die();
        }
    }
}

echo "CLEAN";
