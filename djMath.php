<?php
/**
 * @Author: JacobSamro
 * @Date:   2015-02-11 18:39:46
 * @Last Modified by:   JacobSamro
 * @Last Modified time: 2015-02-11 18:51:56
 */

class djMath{

public function pOfShares($total,$individual){
		return (100/$total)*$individual;
	}

public function	pOfDiscount($total,$discount){
		return $discount/($total/100);
	}

public function	totalAmount($dAmount,$pDiscount){
		return ($dAmount/$pDiscount)*100;
	}

public function	discountAmount($perDiscountPercentage,$pDiscount){
		return $perDiscountPercentage*$pDiscount;
	}		

}