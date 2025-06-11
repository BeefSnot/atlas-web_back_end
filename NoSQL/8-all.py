#!/usr/bin/env python3
"""
Module with MongoDB using pymongo
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents
    """
    documents = []

    for doc in mongo_collection.find():
        documents.append(doc)

    return documents
