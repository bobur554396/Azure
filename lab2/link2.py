# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-20 16:24:01
# @Last Modified by:   bobur
# @Last Modified time: 2017-05-20 16:48:01



from azure.storage.queue import QueueService



queue_service = QueueService(account_name='bobur', account_key='6e60FZapOXAmUbFBw0SpE1lHRP3RkXOMYRaalWmRBoz4+xI5tvjaJzxXuYyt+yfWxjPXpz5X3PmyIFiQmSkjbw==')





######################### Create a Queue  #########################

# queue_service.create_queue('taskqueue')



######################### Insert a Message into a Queue #########################


# for i in range(0, 10):
# 	s = "hello " + str(i)
# 	queue_service.put_message('taskqueue', s.decode('utf-8'))





# messages = queue_service.peek_messages('taskqueue')

# for message in messages:
#     print(message.content)





# messages = queue_service.get_messages('taskqueue')
# for message in messages:
#     queue_service.delete_message('taskqueue', message.id, message.pop_receipt)


# messages = queue_service.get_messages('taskqueue', num_messages=16, visibility_timeout=5*60)
# for message in messages:
#     print(message.content)
    # queue_service.delete_message('taskqueue', message.id, message.pop_receipt)





# metadata = queue_service.get_queue_metadata('taskqueue')
# count = metadata.approximate_message_count




# queue_service.delete_queue('taskqueue')










