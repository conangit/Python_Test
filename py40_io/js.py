#/usr/bin/env python3

import json

'''
d = dict(name='lihong', age=27, score=90)
print(json.dumps(d))

with open('./tmp.txt', 'w') as f:
	json.dump(d, f)

str1 = '{"age":20, "name":"lihong"}'
str2 = 'I am lihong'
print(json.loads(str1))
#print(json.loads(str2))    #error
'''

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
s = Student('lihong', 27, 88)
#print(json.dumps(s))

def StudentToDict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

print(json.dumps(StudentToDict(s)))

