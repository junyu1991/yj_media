#!encoding:utf-8

import os
import hashlib
from sqlalchemy import Column,Integer,String,create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()


class File_info(Base):
    __tablename__='file_info'

    id=Column(Integer,primary_key=True)
    path=Column(String(128),nullable=False)
    md5=Column(String(128),nullable=False)
    ip=Column(String(16),nullable=False)

    def __repr__(self):
        return "Filename:%s" % self.path


class db_tool:
    def __init__(self):
        sql_uri=get_sql_uri()
        engine=create_engine(sql_uri,echo=True)
        _Session=sessionmaker(bind=engine)
        self.session=_Session()

    def add_all_table(self):
        try:
            Base.metadata.create_all(self.engine)
        except:
            print("Create table fail")

    def drop_all_table(self):
        try:
            Base.metadata.drop_all(self.engine)
        except:
            print("Drop table fail")

    def add(self,Object):
        try:
            self.session.add(Object)
            self.commit()
        except Exception,e:
            print("Add object %s fail" % str(Object))
            self.session.rollback()

    def add_all(self,object_list):
        try:
            self.session.add_all(object_list)
            self.session.commit()
        except Exception,e:
            print("Add object list fail")
            self.session.rollback()

    def delete(self,Object):
        try:
            self.session.delete(Object)
            self.session.commit()
        except:
            print("Delete object fail")
            self.session.rollback()

def get_sql_uri():
    return 'mysql://root:test@192.168.1.101/test'

def add_file_info():
    t=db_tool()
    dir_path='/home/test/'
    path=[]
    files=[]
    path.append(dir_path)
    while path:
        temp=path.pop()
        for tf in os.listdir(temp):
            tf=os.path.join(temp,tf)
            if os.path.isdir(tf):
                path.append(tf)
            else:
                file_md5=get_file_md5(tf)
                if file_md5:
                    tfi=File_info(path=tf,md5=file_md5,ip=get_ip())
                    files.append(tfi)
    t.add_all(files)

def get_file_md5(file_name):
    if os.path.exists(file_name):
        md5_object=hashlib.md5()
        with open(file_name,'rb') as f:
            md5_object.update(f.read(1024*1024))
        return md5_object.hexdigest()
    else:
        return None

def get_ip():
    return '127.0.0.1'

if __name__=='__main__':
    engine=create_engine(get_sql_uri(),echo=True)
    Base.metadata.create_all(engine)
    add_file_info()
