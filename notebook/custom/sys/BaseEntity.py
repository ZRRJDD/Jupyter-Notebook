# -*- coding: utf-8 -*-
# Name:         BaseEntity
# Description:  
# Author:       zrrjdd
# Date:         2022/3/20
from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime

# 创建基类
base = declarative_base()

class BaseEntity(base):
    __abstract__ = True

    id = Column(String(64),primary_key=True,nullable=False)
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_date = Column(Date)
    update_date = Column(Date)
    del_flag = Column(String(1),default="0")

    def __init__(self):
        print('init')

    def pre_insert(self):
        now = datetime.datetime.today()
        self.id = str(uuid.uuid4())
        self.create_date = now
        self.update_date = now
        self.create_by = "1"
        self.update_by = '1'

    def pre_update(self):
        now = datetime.datetime.today()
        self.update_date = now
        self.update_by = '1'

