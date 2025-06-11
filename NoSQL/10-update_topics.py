#!/usr/bin/env python3
"""
Module for updating school topics in MongoDB
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name (str): School name to update
        topics (list): List of topic strings
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
