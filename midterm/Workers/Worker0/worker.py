# -*- coding: utf-8 -*-
import os
import datetime
import base64
from time import sleep
from random import randint
from BlobBase import BlobBase
from TableBase import TableBase
from QueueBase import QueueBase

if __name__ == '__main__':
    queue = QueueBase()
    blob = BlobBase()
    table = TableBase()

    while True:
        ## step 1 get generator id from queue
        messages = queue.get_messages_from_queue('generatorsqueue')
        if len(messages) > 0:
            generator_id = messages[0].content

            queue.delete_message_from_queue('generatorsqueue', messages[0])


            ## step 2 generate numbers    
            print('generating numbers ... \n')
            numbers = ""
            for i in range(0, 10):
                rand = randint(0,100)
                numbers += str(rand) + "\n"


            ## step 3 save generated numbers with generator id into blob and get url
            day = datetime.datetime.now().strftime("%Y-%m-%d")
            blob_name = generator_id + "_" + day
            url = blob.save_text_to_blob('generatedfiles', blob_name, numbers)
    

            ## step 4 save url into queue
            data = {'id': generator_id, 'url': url, 'day': day }
            data = str(data)
            print data            
            queue.save_message_to_queue('bloburlsqueue', data)


            ## step 5 add empty row into table
            partition_key = generator_id
            row_key = day
            table.add_empty_row('resulttable', partition_key, row_key, 0)   

        print('-'*20+'worker 0 one loop'+'-'*20)
        sleep(1.0)

