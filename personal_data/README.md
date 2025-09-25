Personal Data Utilities

This folder contains solutions for handling personal data safely:

- filtered_logger.py: Redacts PII fields (name, email, phone, ssn, password) from logs using a custom RedactingFormatter.
- encrypt_password.py: Hashes and verifies passwords using bcrypt.

Notes
- Logger format follows: [HOLBERTON] %(asctime)s %(levelname)s %(name)s: %(message)s
- get_db() reads credentials from env vars: PERSONAL_DATA_DB_USERNAME, PERSONAL_DATA_DB_PASSWORD, PERSONAL_DATA_DB_HOST, PERSONAL_DATA_DB_NAME.
- mysql-connector-python is imported inside get_db() so the module can be imported even if MySQL isn’t installed.