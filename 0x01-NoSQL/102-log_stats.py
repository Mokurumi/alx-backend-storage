#!/usr/bin/env python3
'''
log stats
'''


from pymongo import MongoClient


def log_stats():
    '''
    log_stats method
    '''
    # localhost
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    total = collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
