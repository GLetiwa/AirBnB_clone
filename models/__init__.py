#!/usr/bin/python3
"""
    init module
    - Converts directory and its content into a package
    - Contains an instance of  'FileStorage'
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
