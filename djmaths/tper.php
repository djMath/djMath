<?php
$tp=$_POST['price'];
$da=$_POST['discount'];
$opd=$tp/100;
$dper=$da/$opd;
echo 'The total discount is:' .$dper;
?>
