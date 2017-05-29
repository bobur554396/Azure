# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-20 17:59:28
# @Last Modified by:   bobur554395
# @Last Modified time: 2017-05-22 12:18:47


import datetime
from azure.storage.table import TableService, Entity


# table_service.create_table('generateddata')


class TableBase(object):
	"""docstring for TableBase"""
	
	def __init__(self):
		super(TableBase, self).__init__()
		self.table_service = TableService(account_name='bobur', account_key='6e60FZapOXAmUbFBw0SpE1lHRP3RkXOMYRaalWmRBoz4+xI5tvjaJzxXuYyt+yfWxjPXpz5X3PmyIFiQmSkjbw==')
		

	def add_empty_row(self, table, partition_key, row_key, status):
		print('adding empty row to table...\n')
		row = { 'PartitionKey': partition_key, 'RowKey': row_key, 'result': '', 'status': status}
		self.table_service.insert_or_replace_entity(table, row)


	def update_row_with_result(self, table, partition_key, row_key, sum, status):
		print('updating table row with result...\n')

		xml = '<?xml version="1.0"?><sum>'+str(sum)+'</sum>'

		row = { 'PartitionKey': partition_key, 'RowKey': row_key, 'result': xml, 'status': status}
		self.table_service.update_entity('datatable', row)
