#!/usr/bin/python3
from models.base_model import BaseModel

bm = BaseModel()
s_bm = str(bm)
print(s_bm.split(" ")[0])
print(s_bm.split(" ")[1] == "({})".format(bm.id))
