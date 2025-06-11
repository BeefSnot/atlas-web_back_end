#!/usr/bin/env python3
"""
Module for working with MongoDB using pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: pymongo collection object
        **kwargs: Key-value pairs for the document to insert

    Returns:
        The new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    
    return result.inserted_id
