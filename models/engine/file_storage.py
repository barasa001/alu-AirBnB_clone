#!/usr/bin/python3
"""For the filestorage"""
import os.path
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding= 'utf-8') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        try:
            with open (FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = {key: obj.__class__(**value) for key, value in json.load(f).items()}
        except FileNotFoundError:
            pass
