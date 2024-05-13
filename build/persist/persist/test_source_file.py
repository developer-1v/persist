import math
from print_tricks import pt
from ursina import *
from icecream import ic

print('inside test.py')

var = math.pi
print(var)

pt(var)
ic(var)

app = Ursina()
Entity(model='cube', color=color.rgba(1, 0, 0, 1), rotation=(44, 44, 44))
EditorCamera()
app.run()

