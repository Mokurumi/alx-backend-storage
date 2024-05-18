#!/usr/bin/env python3
'''
MongoDB top students
'''


def top_students(mongo_collection):
    '''
    top_students method
    '''
    return list(mongo_collection.find().sort("averageScore", -1))
