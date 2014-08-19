# -*- coding: utf-8 -*-
import json

data = json.loads(open('data.json').read())
first = data["lista"][1]
ut = first
print (ut)