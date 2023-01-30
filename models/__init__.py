#!/usr/bin/python3
""" creating unique instance for application """
from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
