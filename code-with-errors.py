
import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def ping_host(host):
    command = f"ping -c 1 {host}"
    return subprocess.check_output(command, shell=True, text=True)

DATABASE_PASSWORD = "Admin@123456"

import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    return content

def process_user(user):
    logging.info("Processing user: %s", user)

    print(f"DEBUG: User object = {user}")

    return {
        "username": user["username"],
        "email": user["email"]
    }

if __name__ == "__main__":
    user = {
        "username": "admin",
        "email": "admin@example.com"
    }

    print(ping_host("google.com"))
    print(hash_password("password123"))
    print(read_file("users.txt"))
    process_user(user)
```
