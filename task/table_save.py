# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-20 17:59:28
# @Last Modified by:   bobur
# @Last Modified time: 2017-05-22 12:02:44



import datetime
from azure.storage.table import TableService, Entity


# table_service.create_table('generateddata')


class TableBase(object):
	"""docstring for TableBase"""
	
	def __init__(self):
		super(TableBase, self).__init__()
		self.table_service = TableService(account_name='bobur', account_key='6e60FZapOXAmUbFBw0SpE1lHRP3RkXOMYRaalWmRBoz4+xI5tvjaJzxXuYyt+yfWxjPXpz5X3PmyIFiQmSkjbw==')
		

	def create_empty_row(self, status):
		print 'adding empty row to table...\n'
		date = datetime.datetime.now().strftime("%Y-%m-%d")
		generator = 'G1_' + date
		row = { 'PartitionKey': generator, 'RowKey': date, 'result': '', 'status': status}
		self.table_service.insert_or_replace_entity('datatable', row)


	def set_result(self, sum, status):
		print 'updating table row with result...\n'
		date = datetime.datetime.now().strftime("%Y-%m-%d")
		generator = 'G1_' + date
		row = { 'PartitionKey': generator, 'RowKey': date, 'result': '<sum>'+str(sum)+'</sum>', 'status': status}
		self.table_service.update_entity('datatable', row)


