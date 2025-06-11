#!/usr/bin/env python3
"""
Module for finding schools by topic in MongoDB
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): Topic to search for

    Returns:
        List of school documents matching the topic
    """
    return list(mongo_collection.find({"topics": topic}))
