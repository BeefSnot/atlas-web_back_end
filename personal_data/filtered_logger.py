#!/usr/bin/env python3
"""filtered_logger module.

Provides helpers to safely log records while redacting PII fields,
connect to a MySQL database from environment variables, and dump
user rows with redacted fields.
"""
from __future__ import annotations

import logging
import os
import re
from typing import Iterable, Tuple

import mysql.connector
from mysql.connector.connection import MySQLConnection


PII_FIELDS: Tuple[str, ...] = (
    "name",
    "email",
    "phone",
    "ssn",
    "password",
)


def filter_datum(fields: Iterable[str], redaction: str,
                  message: str, separator: str) -> str:
    """Obfuscate values of specified fields in a log line.

    Uses a single regex substitution to replace any value appearing after
    "field=" up to the next separator with the provided redaction string.
    """
    pattern = (r"(?P<field>" + "|".join(map(re.escape, fields)) + r")="
               r"[^" + re.escape(separator) + r"]*")
    return re.sub(pattern,
                  lambda m: f"{m.group('field')}={redaction}",
                  message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that masks PII fields in messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Iterable[str]):
        """Initialize formatter with fields to redact."""
        super().__init__(self.FORMAT)
        self.fields = tuple(fields)

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with PII redacted."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Create and configure a logger for user data with redaction.

    Returns a logger named "user_data" at INFO level, with a single
    StreamHandler using RedactingFormatter parameterized by PII_FIELDS.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
        logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """Create a connection to the MySQL database using env variables.

    Env variables (with defaults):
      - PERSONAL_DATA_DB_USERNAME (default: "root")
      - PERSONAL_DATA_DB_PASSWORD (default: "")
      - PERSONAL_DATA_DB_HOST (default: "localhost")
      - PERSONAL_DATA_DB_NAME (no default; required)
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name,
    )


def main() -> None:
    """Obtain DB connection and log all users with redacted PII fields."""
    fields = (
        "name", "email", "phone", "ssn", "password",
        "ip", "last_login", "user_agent",
    )
    query = (
        "SELECT name, email, phone, ssn, password, ip, last_login, user_agent"
        " FROM users;"
    )

    logger = get_logger()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query)

    try:
        for row in cur:
            message = "; ".join(f"{k}={v}" for k, v in zip(fields, row)) + ";"
            logger.info(message)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
