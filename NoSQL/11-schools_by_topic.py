#!/usr/bin/env python3
""" Search School """
import pymongo


def schools_by_topic(mongo_collection, topic: str):
    """ 
    function that returns the list of school having a specific
    """
    query: dict = {"topics": topic}
    schools: list = []

    for school in mongo_collection.find(query):
        schools.append(school)

    return schools
