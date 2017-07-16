# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-22 10:28:48
# @Last Modified by:   bobur554395
# @Last Modified time: 2017-07-15 14:36:50


from azure.storage.blob import BlockBlobService, ContentSettings


# block_blob_service.create_container('generatedfiles')


class BlobBase(object):
	"""docstring for BlobBase"""
	
	def __init__(self):
		super(BlobBase, self).__init__()
		self.block_blob_service = BlockBlobService(account_name='boburstorage', account_key='wRgukLsyhLtnI7qEk8mSGnIBC+IsiTTXEDF1/xnmBGDudJLSeYdtyuVzuSN5/cplJz88AJPyoVyjCmL9N1ECXw==')

	def save_text_to_blob(self, container, blob_name, text):
		print('saving blob into container...\n')
		self.block_blob_service.create_blob_from_text(
			container,
			blob_name,
			text,
			content_settings=ContentSettings(content_type='text/plain'))

		url = self.block_blob_service.make_blob_url(container, blob_name)
		return url

	
		
