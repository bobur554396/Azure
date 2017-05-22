# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-20 17:42:41
# @Last Modified by:   bobur554395
# @Last Modified time: 2017-05-22 12:20:31



from random import randint



class Generator(object):
	"""docstring for Generator"""
	
	def __init__(self):
		super(Generator, self).__init__()
		

	def generateData1():
		print '(G1) generating random numbers...\n'
		with open('data.txt', 'w+') as f:
			for i in range(0, 10):
				rand = randint(0,100)
				f.write(str(rand) + "\n")