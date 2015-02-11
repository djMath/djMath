<?php
$da=$_POST['discount'];
$dp=$_POST['dis_per'];
$tot=($da/$dp)*100;
echo 'Total Price is:' .$tot;
?>