#!/usr/bin/python3
""" __init__.py method for model package """
from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
