# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-20 17:49:46
# @Last Modified by:   bobur554395
# @Last Modified time: 2017-05-22 12:20:01


from generator import Generator
from table_save import TableBase
from queue_save import QueueBase
from blob_save import BlobBase




# generate random numbers and save to file
generator = Generator()
generator.generateData1()





# blob storage
blob = BlobBase()

url = blob.save_file_to_blob()




# queue storage
queue = QueueBase()

queue.save_to_queue(url)





# table storage
table = TableBase()

table.create_empty_row(0)









