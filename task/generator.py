# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-20 17:42:41
# @Last Modified by:   bobur
# @Last Modified time: 2017-05-22 11:57:58



from random import randint




def generateData():
	print 'generating random numbers...\n'
	with open('data.txt', 'w+') as f:
		for i in range(0, 10):
			rand = randint(0,100)
			f.write(str(rand) + "\n")