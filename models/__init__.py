#!/usr/bin/python3
'''
Module __init__
Initilises a package
'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
