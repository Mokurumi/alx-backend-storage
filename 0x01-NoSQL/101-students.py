#!/usr/bin/env python3
'''
MongoDB top students
'''


def top_students(mongo_collection):
    '''
    top_students method
    '''
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])