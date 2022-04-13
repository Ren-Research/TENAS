#!/usr/bin/env python3

import numpy as np
import torch
import pickle

depth = 6
dim = 5

arr = []

for l1 in range(dim):
	for l2 in range(dim):
		for l3 in range(dim):
			for l4 in range(dim):
				for l5 in range(dim):
					for l6 in range(dim):
						arr.append([l1, l2, l3, l4, l5, l6])
						#print([l1, l2, l3, l4, l5, l6])

all_arch = []
for i in range(len(arr)):
	config = arr[i]
	t = [[-1000] * dim for _ in range(depth)]
	for j in range(len(config)):
		t[j][config[j]] = 0
	#print(t)
	t = torch.tensor(np.array(t))
	all_arch.append(t)
print(all_arch)
	
pickle.dump(all_arch, open("all_arch.pickle", "wb"))  # save it into a file named save