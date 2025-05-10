#!/usr/bin/env python3
"""
Task 1
Module providing string manipulation utilities.
Contains a type-annotated function for string concatenation.
"""


def concat(str1: str, str2: str) -> str:
    """
    Join two strings together.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        A new string containing str1 followed by str2
    """
    return str1 + str2