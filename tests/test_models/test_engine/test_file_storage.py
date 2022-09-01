#!/usr/bin/python3
"""
This module include test for the file_stotage.py
"""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_basic(unittest.TestCase):
    """For testing the basics of the FileStorage class"""
    
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        
    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
            
    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)
        
class TestFileStorage_methods(unittest.TestCase):
    """For testing the methods of the FileStorage class"""
    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
      new_model = BaseModel()
      models.storage.new(new_model)
      self.assertIn("BaseModel." + new_model.id, models.storage.all().keys())
      self.assertIn(new_model, models.storage.all().values())
      
    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)
            
    def test_save(self):
        new_model = BaseModel()
        models.storage.new(new_model)
        model.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
    
    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)
            
    def test_reload(self):
        new_model = BaseModel()
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + new_model.id, objs)
        
    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)
            
           
 
if __name__ == "__main__":
    unittest.main()
