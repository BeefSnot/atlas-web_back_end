#!/usr/bin/env python3
"""
Module for handling personal data
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, 
                separator: str) -> str:
    """
    Obfuscates specified fields in a log message
    """
    for field in fields:
        pattern = f'{field}=.*?{separator}'
        repl = f'{field}={redaction}{separator}'
        message = re.sub(pattern, repl, message)
    return message
