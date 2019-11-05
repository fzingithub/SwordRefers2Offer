# merge sort 2019/3/29
import numpy as np
import time

class Sort:
	def merge_sort(self, array):
		if len(array) < 2:
			return array

		midd = len(array)//2
		left = self.merge_sort(array[:midd])
		right = self.merge_sort(array[midd:])
		return self.merge(left, right)

	def merge(self, left, right):
		res = []
		while left and right:
			res.append(left.pop(0)) if left[0]>right[0] else res.append(right.pop(0))

		res.extend(left) if left else res.extend(right)
		return res

if __name__ == '__main__':
	randomNum = np.random.randint(0, 100, size=60)

	test = Sort()
	start = time.time()
	res = test.merge_sort(list(randomNum))
	end = time.time()

	print('time', end - start)
	print(res)