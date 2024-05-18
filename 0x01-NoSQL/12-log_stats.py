#!/usr/bin/env python3
'''
MongoDB log stats
'''


def log_stats(mongo_collection):
    '''
    log_stats method
    '''
    print(f"{mongo_collection.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {mongo_collection.count_documents(
        {'method': 'GET'})}")
    print(f"\tmethod POST: {mongo_collection.count_documents(
        {'method': 'POST'})}")
    print(f"\tmethod PUT: {mongo_collection.count_documents(
        {'method': 'PUT'})}")
    print(f"\tmethod PATCH: {mongo_collection.count_documents(
        {'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {mongo_collection.count_documents(
        {'method': 'DELETE'})}")
    print(f"{mongo_collection.count_documents(
        {'method': 'GET', 'path': '/status'})} status check")
