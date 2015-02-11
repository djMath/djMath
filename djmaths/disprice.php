<?php
$tp=$_POST['price'];
$dp=$_POST['dis_per'];
$opd=$tp/100;
$tdp=$opd*$dp;
echo 'Discount price is:' .$tdp;
?>