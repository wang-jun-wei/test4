# coding: utf-8
"""
Created On 2019/3/13 10:24

@author : wjw
"""
import datetime

date = "2019-03-13 10:02:20"
date1 = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
print(date1)