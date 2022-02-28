#!/usr/bin/python3
from models.engine.file_storage import *
from models.base_model import BaseModel

all_objs = Filestorage()
print("-- Reloaded objects --")
print("{}".format(all_objs.all()))

