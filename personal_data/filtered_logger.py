#!/usr/bin/env python3
"""Personal data logging with PII redaction.

Implements:
- filter_datum: redact selected fields in log messages
- RedactingFormatter: logging.Formatter that applies filter_datum
- get_logger: preconfigured logger using RedactingFormatter
- get_db: connect to MySQL using env vars
- main: read users table and log rows with redaction
"""

import logging
import os
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str],
    redaction,
    message,
    separator,
):
    """Return the log message with specified fields redacted.

    Each key=value pair separated by `separator` will have value replaced by
    `redaction` if key is in `fields`.
    """
    pattern = (
        r"(" + "|".join(re.escape(f) for f in fields) + r")=([^"
        + re.escape(separator)
        + r"]*)"
    )
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Formatter that redacts PII fields from log records."""

    REDACTION = "***"
    FORMAT = (
        "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    )
    SEPARATOR = ";"

    def __init__(self, fields) -> None:
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record):
        msg_str = str(record.getMessage())
        record.msg = filter_datum(
            self.fields, self.REDACTION, msg_str, self.SEPARATOR
        )
        return super().format(record)


def get_logger() -> logging.Logger:
    """Create and return a logger configured for user data."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        logger.addHandler(handler)

    return logger


def get_db():
    """Return a MySQL DB connection using env vars.

    Env vars used:
    - PERSONAL_DATA_DB_USERNAME (default: "root")
    - PERSONAL_DATA_DB_PASSWORD (default: "")
    - PERSONAL_DATA_DB_HOST (default: "localhost")
    - PERSONAL_DATA_DB_NAME (required)
    """
    import mysql.connector

    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username, password=password, host=host, database=database
    )


def main():
    """Obtain a DB connection and log all rows from the users table."""
    logger = get_logger()
    try:
        db = get_db()
    except Exception:
        return

    cursor = db.cursor()
    cursor.execute(
        (
            "SELECT name, email, phone, ssn, password, "
            "ip, last_login, user_agent FROM users;"
        )
    )
    fields = (
        "name", "email", "phone", "ssn", "password",
        "ip", "last_login", "user_agent",
    )
    for row in cursor:
        message = "; ".join(
            f"{k}={v}" for k, v in zip(fields, row)
        ) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
