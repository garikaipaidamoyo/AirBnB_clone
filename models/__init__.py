#!/usr/bin/python3
<<<<<<< HEAD
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

=======
"""Initialize the package"""

from models.engine.file_storage import FileStorage
>>>>>>> test_branch

storage = FileStorage()
storage.reload()
