#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from enum import Enum, unique

Week = Enum('Week', ('Mon.', 'Tues.', 'Wed.', 'Thur.', 'Fri.', 'Sat.', 'Sun.'))

print(dir(Week))

for name, member in Week.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Color(Enum):
    Red = 0
    Black = 1
    Blue = 2
    Green = 3
    Yellow = 4

c1 = Color.Black
print(c1)
print(Color.Green)
print(Color['Blue'])
print(Color.Green.value)
print(Color(2))

for its in Color.__members__.items():
    print(its)

for name, member in Color.__members__.items():
    print(name, member, member.value)

