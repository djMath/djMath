/* 
* @Author: JacobSamro
* @Date:   2015-02-10 19:08:24
* @Last Modified by:   JacobSamro
* @Last Modified time: 2015-02-10 19:39:24
*/

'use strict';


var djMath = {
	pOfShares: 	function(total,individual){
		return (100/total)*individual;
	},
	pOfDiscount: function(total,discount){
		return discount/(total/100);
	},
	totalAmount: function(dAmount,pDiscount){
		return (dAmount/pDiscount)*100;
	},
	discountAmount: function(perDiscountPercentage,pDiscount){
		return perDiscountPercentage*pDiscount
	}		
};