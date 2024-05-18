#!/usr/bin/env python3
'''
MongoDB get all documents
'''


def list_all(mongo_collection):
    '''
    list_all method
    '''
    return list(mongo_collection.find())
