#/usr/bin/env python3

import pickle

d = dict(name='bob', age=20, score=88)
print(pickle.dumps(d))

with open('./tmp.txt', 'wb') as f:
	pickle.dump(d, f)

with open('./tmp.txt', 'rb') as f1:
	d1 = pickle.load(f1)
print(d1)
