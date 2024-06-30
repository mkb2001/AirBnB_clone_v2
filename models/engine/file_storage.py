#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            return {key: value
                    for key, value in FileStorage.__objects.items()
                    if value.__class__ == cls}
        

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
    def reload(self):
            """Loads storage dictionary from file"""
            from os import path
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
        
            try:
                temp = {}
                with open(FileStorage.__file_path, 'r') as f:
                    if path.getsize(FileStorage.__file_path) == 0:
                        pass
                    else:
                        temp = json.load(f)
                        for key, val in temp.items():
                            self.all()[key] = classes[val['__class__']](**val)
            except FileNotFoundError:
                pass

    def delete(self, obj=None):
        """ Deletes an object from the file storage based on the name
        """
        if obj is None:
            pass
        else:
            objects_copy = FileStorage.__objects.copy()
            for key, value in FileStorage.__objects.items():
                if value.name == obj.name:
                    del FileStorage.__objects[key]
                    break