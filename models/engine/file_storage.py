#!/usr/bin/python3
"""
This module is used for serialization and deserialization of json file 
"""

import json
from models.user import User
from models.base_model import BaseMode

class FileStorage:
  """
  custom class for file storage
    
  Private class attributes: 
      __file_path(str): path to the JSON file
      __objects(dict): to store all objects by <class name>.id
    
  Public instance methods:
      all(self): returns the dictionary __objects
      new(self, obj): sets in __objects the obj with key <obj class name>.id
      save(self): serializes __objects to the JSON file (path: __file_path)
      reload(self): deserializes the JSON file to __objects
      
  """
  
  __filepath = "file.json"
  __objects = {}
  
  def all(self):
    """
    Returns the dictionary __objects
    """
    return self.__objects
 
 def new(self, obj):
    """
    Sets in __objects the obj with key <obj class name>.id
    
    Args:
        obj(object): object to set
        
    """
    self.__objects[object.__class__.__name__+'.'+str(obj)] = obj
    
 def save(self):
    """
    serializes __objects to the JSON file
    """
    with open(self.__file_path, 'w+') as f:
        json.dump({key: self.__objects[key].to_dict() for k key in self.__objects}, f)
        
 def reload(self):
    """
    deserializes the JSON file to __objects
    """
    try:
        with open(self.__file_path, 'r') as f:
            obj_dict = json.loads(f.read())
            for value in obj_dict.values():
                self.new(eval(value["__class__"])(**value))
    except Exception:
        pass
