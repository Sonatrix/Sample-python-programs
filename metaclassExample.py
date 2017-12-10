#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 13:46:29 2017

@author: praveen
"""

class CustomMetaClass(type):
    def __init__(cls,name,bases,dct):
        print('create class {0} with metaclass base class {1}'.format(name,bases))
        super(CustomMetaClass,cls).__init__(name,bases,dct)

#define new cstom class
class CustomBase(object,metaclass = CustomMetaClass):
    pass


class Base1(CustomBase):
    pass
    