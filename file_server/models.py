#!encoding:utf-8

from flask import Column,Integer,String,Date

from flask.ext.declarative import declarative_base

Base=declarative_base()


class Category(Base):
    __tablename__='category'

    id=Column(Integer,primary_key=True,autoincrement=False)
    category_name=Column(String(128),nullable=False)
    parent=Column(Integer)

    def __repr__(self):
        return self.__tablename__


class File_Info(Base):
    __tablename__='file_info'

    id=Column(Integer,primary_key=True)
    file_path=Column(String(512),nullable=False)
    file_name=Column(String(128),nullable=False)
    file_md5=Column(String(128),nullable=False)
    server_no=Column(Integer,nullable=False)
    file_size=Column(Integer)

    def __repr__(self):
        return self.__tablename__

class Server_Info(Base):
    __tablename__='server_info'

    server_no=Column(Integer,primary_key=True,autoincrement=False)
    server_ip=Column(String(32),nullable=False)
    server_port=Column(Integer,nullable=False,default=9966)
    server_mac=Column(String(128))

    def __repr__(self):
        return self.__tablename__

class User(Base):
    __tablename__='User'

    id=Column(Integer,primary_key=True)

    name=Column(String(32),nullable=False)
    password=Column(String(128),nullable=False)
    lastlogondate=Column(Date)
    lastlogonip=Column(String(32))

    role_id=Column(Integer,nullable=False)

    def __repr__(self):
        return self.__tablename__

class Role(Base):
    __tablename__='role'

    id=Column(Integer,primary_key=True,autoincrement=False)

    role_name=Column(String(32),nullable=False)


class Comments(Base):
    __tablename__='comments'

    id=Column(Integer,primary_key=True)
    file_id=Column(Integer,nullable=False)
    comment_text=Column(Text,nullable=False)
    comment_date=Column(Date,nullable=False)
    comment_user_id=Column(Integer,nullable=False)
    comment_ip=Column(String(32),nullable=False)
    deleted=Column(Integer,nullalbel=False,default=0) #0:not deleted,-1:deleted

    def __repr__(self):
        return self.__tablename__


