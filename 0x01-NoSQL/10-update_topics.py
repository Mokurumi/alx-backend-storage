#!/usr/bin/env python3
'''
MongoDB update collections that match
'''


def update_topics(mongo_collection, name, topics):
    '''
    update_topics method
    '''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
