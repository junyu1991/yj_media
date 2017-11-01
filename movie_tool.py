#!/usr/bin/env python
#!encoding:utf-8

import os
import socket
import threading

from sqlalchemy import create_engine

class ReadFileThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)



def read_file(file_path,start,end):
    if not os.path.exists(file_path):
        return None
    if start>=end:
        return None
    file_size=os.path.getsize(file_path)
    if start>file_size:
        return None
    read_buf=end-start
    if file_size<read_buf:
        read_buf=file_size-start
    f=file(file_path)
    f.seek(start)
    result=f.read(read_buf)
    f.close()
    return result

def handle_client(client):
    pass
