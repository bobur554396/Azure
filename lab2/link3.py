# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-20 16:48:17
# @Last Modified by:   bobur
# @Last Modified time: 2017-05-20 17:10:26


from azure.storage.blob import BlockBlobService


block_blob_service = BlockBlobService(account_name='bobur', account_key='6e60FZapOXAmUbFBw0SpE1lHRP3RkXOMYRaalWmRBoz4+xI5tvjaJzxXuYyt+yfWxjPXpz5X3PmyIFiQmSkjbw==')


# block_blob_service.create_container('mycontainer')



# from azure.storage.blob import PublicAccess
# block_blob_service.create_container('mycontainer', public_access=PublicAccess.Container)

# block_blob_service.set_container_acl('mycontainer', public_access=PublicAccess.Container)





# from azure.storage.blob import ContentSettings

# block_blob_service.create_blob_from_path(
#     'mycontainer',
#     'myblockblob',
#     '1.png',
#     content_settings=ContentSettings(content_type='image/png')
#     )
    




# generator = block_blob_service.list_blobs('mycontainer')
# for blob in generator:
#     print(blob.name)


# block_blob_service.get_blob_to_path('mycontainer', 'myblockblob', 'out-sunset.png')


# block_blob_service.delete_blob('mycontainer', 'myblockblob')





from azure.storage.blob import AppendBlobService

append_blob_service = AppendBlobService(account_name='bobur', account_key='6e60FZapOXAmUbFBw0SpE1lHRP3RkXOMYRaalWmRBoz4+xI5tvjaJzxXuYyt+yfWxjPXpz5X3PmyIFiQmSkjbw==')

# The same containers can hold all types of blobs
append_blob_service.create_container('myappendcontainer')

# Append blobs must be created before they are appended to
append_blob_service.create_blob('myappendcontainer', 'myappendblob')
append_blob_service.append_blob_from_text('myappendcontainer', 'myappendblob', u'Hello, world!')

append_blob = append_blob_service.get_blob_to_text('myappendcontainer', 'myappendblob')

print append_blob.content

