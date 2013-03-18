# -*- coding: utf-8 -*-

"""
Some utility functions
"""
import time
import datetime


def timestamp_utcnow():
    now = datetime.datetime.now()
    return time.mktime(now.timetuple())
