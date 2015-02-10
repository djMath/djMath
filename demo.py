#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: JacobSamro
# @Date:   2015-02-10 19:18:47
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-02-10 19:33:48

from djMath import *

# Percentage of Shares of an Indiviual user
# Syntax :: pOfShares(Total Amount ,Individual Amount)
print(djMath.pOfShares(100,10))

# Percentage of Discount
# Syntax :: pOfDiscount(Total Amount,Discount Amount)
print(djMath.pOfDiscount(7000,1000))

# Finding Total Amount from Discount and Percentage of Discount
# Syntax :: totalAmount(Discount Amount,Percentage of Discount)
print(djMath.totalAmount(1000,14.28))

# Finding Discount Amount with  Amount of 1% and Discount Percentage 
# Syntax :: totalAmount(Amount of 1%,Discount Percentage)
print(djMath.discountAmount(70,14.28))