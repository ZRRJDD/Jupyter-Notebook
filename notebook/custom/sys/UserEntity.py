# -*- coding: utf-8 -*-
# Name:         UserEntity
# Description:  
# Author:       zrrjdd
# Date:         2022/3/20
from .BaseEntity import BaseEntity
from sqlalchemy import Column,String,Date

class User(BaseEntity):

    __tablename__ = 'sys_user'

    login_name = Column(String(32),nullable=False)
    name = Column(String(32),nullable=False)
    password = Column(String(128),nullable=False)

    def __init__(self):
        print('User Init')

    def __init__(self, login_name, name):
        self.login_name = login_name
        self.name = name

    def set_password(self,password):
        self.password = password

    def get_password(self):
        return self.password