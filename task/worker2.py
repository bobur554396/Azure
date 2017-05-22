# -*- coding: utf-8 -*-
# @Author: bobur
# @Date:   2017-05-22 10:10:16
# @Last Modified by:   bobur
# @Last Modified time: 2017-05-22 12:01:41

from queue_save import QueueBase
from table_save import TableBase



queue = QueueBase()


numbers = queue.get_data_from_url()
s = 0
for i in range(len(numbers)):
	s += int(numbers[i])


table = TableBase()

table.set_result(s, 1)
