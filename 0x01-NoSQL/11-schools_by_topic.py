#!/usr/bin/env python3
'''
MongoDB get all documents
'''


def schools_by_topic(mongo_collection, topic):
    '''
    schools_by_topic method
    '''
    return mongo_collection.find({"topics": topic})
