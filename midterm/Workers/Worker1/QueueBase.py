# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-22 10:35:39
# @Last Modified by:   bobur554395
# @Last Modified time: 2017-07-16 18:55:45


from azure.storage.queue import QueueService


# queue_service.create_queue('taskqueue')

class QueueBase(object):
	"""docstring for QueueBase"""

	def __init__(self):
		super(QueueBase, self).__init__()
		self.queue_service = QueueService(account_name='boburstorage', account_key='wRgukLsyhLtnI7qEk8mSGnIBC+IsiTTXEDF1/xnmBGDudJLSeYdtyuVzuSN5/cplJz88AJPyoVyjCmL9N1ECXw==')

	def save_message_to_queue(self, queue, data):
		self.queue_service.put_message(queue, data)
		print('url added into queue...\n')


	def get_data_from_url(self):
		print('reading data from blob using url in queue...\n')
		data = self.queue_service.get_messages('taskqueue')


		response = urllib2.urlopen(data[0].content)
		numbers = response.read()

		self.queue_service.delete_message('taskqueue', data[0].id, data[0].pop_receipt)
		return numbers.splitlines()

	def get_messages_from_queue(self, queue):
		return	self.queue_service.get_messages(queue)

	def delete_message_from_queue(self, queue, message):
		self.queue_service.delete_message(queue, message.id, message.pop_receipt)

