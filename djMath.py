#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Authors: JacobSamro , Dhinakaran
# @Date:   2015-02-10 19:07:50
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-02-10 19:34:05

class djMath(object):
	"""DJ Math is a Funny Math Library - For Programmers who are really bad at Math
	It is not a Myth, Try DJ Math"""
	def __init__(self, arg):
		super(djMath, self).__init__()
		self.arg = arg

	def pOfShares(total,individual):
		return (100/total)*individual

	def pOfDiscount(total,discount):
		return discount/(total/100)

	def totalAmount(dAmount,pDiscount):
		return (dAmount/pDiscount)*100

	def discountAmount(perDiscountPercentage,pDiscount):
		return perDiscountPercentage*pDiscount


		