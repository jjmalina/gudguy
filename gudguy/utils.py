# -*- coding: utf-8 -*-

"""
Some utility functions
"""
import time
import datetime


def timestamp_utcnow():
    now = datetime.datetime.now()
    return time.mktime(now.timetuple())


def response_json_or_none(fn):
    def wrapper(*args, **kwargs):
        response = fn(*args, **kwargs)
        return response.json() if response.status_code == 200 else None
    return wrapper
