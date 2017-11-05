#!encoding:utf-8

import hashlib
import os
import socket
import json


def get_file_md5(file_name):
    '''
    Get file md5
    :return md5 string or None if file not exists
    '''
    if os.path.exists(file_name) and os.path.isfile(file_name):
        md5_object=hashlib.md5()
        with open(file_name,'rb') as f:
            temp_data=f.read(1024*1024)
            while temp_data:
                md5_object.update(temp_data)
                temp_data=f.read(1024*1024)
        return md5_object.hexdigest()
    else:
        return None

def get_ip():
    '''
    Get local mechine ip
    :return :ip string
    '''
    ip=socket.gethostbyname(socket.gethostname())
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',56895))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_json(config_file):
    '''
    Get json data from json file
    : return: return None if config_file not exists
    '''
    if not os.path.exists(config_file):
        return None
    with open(config_file,"rb") as f:
        data=json.loads(f.read())
    return data


