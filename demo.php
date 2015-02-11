<?php
/**
 * @Author: JacobSamro & Dhinakaran
 * @Date:   2015-02-11 18:39:46
 * @Last Modified by:   JacobSamro
 * @Last Modified time: 2015-02-11 18:52:49
 */

require("djMath.php");

$djMath = new djMath;


echo $djMath->pOfShares(100,10).'<br/>';
echo $djMath->pOfDiscount(7000,1000).'<br/>';
echo $djMath->totalAmount(1000,14.28).'<br/>';
echo $djMath->discountAmount(70,14.28).'<br/>';

?>