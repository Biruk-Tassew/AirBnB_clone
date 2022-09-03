#!/usr/bin/python3
"""
Test for the base model
"""

import os
import uuid
import time
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """
    Tests the attributes of the base model
    """
    
    def setUp(self):
        """
        Classes needed for testing
        """
        pass
    
    def reset_fileStorage(self):
        """
        Resets the data in FileStorage.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file__path)
    
    def test_basic(self):
        """
        Tests the basic attribute of the BaseModel class
        """
        new_model = BaseModel()
        new_mode.id = str(uuid.uuid4())
        new_model.name = "AirBnB"
        new_model.number = 12
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.name, str)
        self.assertIsInstance(new_model.number, int)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertEqual([new_model.name, new_model.number], ["AirBnB", 12])
        self.assertEqual(str(type(new_model)), "<class 'models.base_model.BaseModel'>")
            
    def test_dict(self):
        """
        Test method for dict
        """
        new_model = BaseModel()
        new_model_dict = new_model.to_dict()
        self.assertIsInstance(new_model_dict, dict)
        self.assertIn('id', new_model_dict.keys())
        self.assertIn('created_at', new_model_dict.keys())
        self.assertIn('updated_at', new_model_dict.keys())
        self.assertEqual(new_model_dict['__class__'], type(new_model).__name__)
        new_model_two = BaseModel(id=str(uuid.uuid4()), name="AirBnB", number=12)
        with self.assertRaises(KeyError) as e:
              new_model_two.to_dict()
            
    def test_save(self):
        """
        Test for save method 
        """
        new_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        new_model.save()
        diff = new_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        
    def test_save_storage(self):
        """
        Tests that storage.save() is called from save()
        """
        new_model = BaseModel()
        new_model.save()
        key = "{}.{}".format(type(new_model).__name__, new_model.id)
        dict = {key: new_model.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(dict)))
            f.seek(0)
            self.assertEqual(json.load(f), dict)

    def test_save_no_args(self):
        """
        Tests the function save with no arguments
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        err_message = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err_message)

    def test_save_excess_args(self):
        """
        Tests the function save with too many arguments
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 12)
        err_message = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), err_message)

    def test_str(self):
        """
        Test method for str representation
        """
        new_model = BaseModel()
        string = f"[{type(new_model).__name__}] ({new_model.id}) {new_model.__dict__}"
        self.assertEqual(new_model.__str__(), string)    
      
if __name__ == '__main__':
    unittest.main()    
      
