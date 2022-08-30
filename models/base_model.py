#!/usr/bin/python3
"""
Base class for AirBnB project
"""

import models
from uuid import uuid4
from datatiem import datatime

class BaseModel:
  """Base class for all classes in the AirBnB console project
  
  Public instance attributes: 
      id(str): to have unique id for each BaseModel - uuid.uuid4() is being used
      created_at(datetime): assign with the current datetime when an instance is created 
      updated_at(datetime): it will be updated every time the object is changed
      
 Public instance methods: 
      save(self): updates updated_at with the current datetime
      to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance
  """
  
  def __init__(self, *args, **kwargs):
    """For initializing the base model
    
    Args:
        *args: positional arguments
        **kwargs: keyword arguments
    """
    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    if kwargs:
      for item in kwargs:
        if item == "updated_at" or item == "created_at":
          self.__dict__[item] = datetime.strptime(kwargs[item], DATE_TIME_FORMAT)
        elif item[0] == "id":
          self.__dict__[item] = str(kwargs[item])
         else:
          self.__dict__[item] = kwargs[item]
    else:
      self.id = str(uuid4())
      self.created_at = datetime.utcnow()
      self.updated_at = datetime.utcnow()
      models.storage.new(self)
      
  def __str__(self):
    """
    Returns string representation of the BaseModel class
    """
    return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)
  
  def save(self):
    """
    updates updated_at with the current datetime
    """
    self.updated_at = datetime.utcnow()
    models.storage.save()
    
  def to_dict(self):
    """
    Returns a dictionary __dict__ of instances
    """
    objects = {}
    for item in self.__dict__:
      if item == "updated_at" or item == "created_at":
        objects[item] = self.__dict__[item].isoformat()
      else:
        objects[item] = self.__dict__[item]
    objects["__class__"] = self.__class__.__name__
    return objects
