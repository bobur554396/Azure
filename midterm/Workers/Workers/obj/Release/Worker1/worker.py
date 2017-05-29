import os
import datetime
import ast
import urllib.request
from time import sleep
from random import randint
from TableBase import TableBase
from QueueBase import QueueBase

if __name__ == '__main__':
    queue = QueueBase()
    table = TableBase()

    while True:
        ## step 1 get url from queue and delete  
        messages = queue.get_messages_from_queue('bloburlsqueue')
        if len(messages) > 0:
            print('getting url from queue...\n')
            data = ast.literal_eval(messages[0].content)
            generator_id = data['id']
            day = data['day']
            url = data['url']
            queue.delete_message_from_queue('bloburlsqueue', messages[0])

            ## step 2 read file and find sum      
            print('calculating sum of numbers...\n')      
            response = urllib.request.urlopen(url)
            numbers = response.read().splitlines()
            sum = 0
            for n in numbers:
                sum += int(n)

            ## step 3 update table with result
            partition_key = generator_id
            row_key = day
            table.update_row_with_result('resulttable', partition_key, row_key, sum, 1)

        print('-'*20+'worker 1 one loop'+'-'*20)
        sleep(1.0)

