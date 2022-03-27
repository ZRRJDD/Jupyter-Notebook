# -*- coding: utf-8 -*-
# Name:         UserUtils
# Description:  
# Author:       zrrjdd
# Date:         2022/3/10
from ..DBUtil import DBFactory
from .UserEntity import User

def getUserById(id):
    dbFactory = DBFactory()
    session = dbFactory.get_session()
    user = session.query(User).filter(User.id == id).first()
    session.commit()
    return user

def getUserByLoginName(loginName):
    dbFactory = DBFactory()
    session = dbFactory.get_session()
    user = session.query(User).filter(User.login_name == loginName).first()
    session.commit()
    return user

def saveUser(user):
    dbFactory = DBFactory()
    session = dbFactory.get_session()
    session.add(user)
    session.commit()

'''
    检查用户名及密码是否正确
'''
def checkUsernameAndPassword(username, password):
    user = getUserByLoginName(username)
    if user is None:
        print('用户不存在')
        return False,None
    '''验证用户名和密码是否正确'''
    if user.get_password() == password:
        return True,user
    return False,None
