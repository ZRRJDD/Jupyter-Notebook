# -*- coding: utf-8 -*-
# Name:         DBUtil
# Description:  获取数据链接等信息
# Author:       zrrjdd
# Date:         2022/3/10
# -*- coding: utf-8 -*-
# Name:         DBUtils
# Description:
# Author:       zrrjdd
# Date:         2022/3/20

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBFactory(object):

    def __init__(self):
        self.session = None
        self.engine = None
        self.conn = None
        self.init_db()

    def init_db(self):
        self.engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/jupyter",
            encoding="utf-8",
            # echo=True # 关闭SQL代码输出
        )

    def get_session(self):
        if self.engine is None:
            self.init_db()
        if self.session is None:
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
        return self.session

    def get_conn(self):
        if self.engine is None:
            self.init_db()
        if self.conn is None:
            self.conn = self.engine.connect()
        return self.conn