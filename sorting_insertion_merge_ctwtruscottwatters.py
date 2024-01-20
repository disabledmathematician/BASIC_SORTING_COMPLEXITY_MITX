import time
def sort(left, right, cmp):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if cmp(left[i], right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result
	
def mergeSort(L, cmp):
	if len(L) < 2:
		return L[:]
	else:
		left = mergeSort(L[:len(L) // 2], cmp)
		right = mergeSort(L[len(L) // 2:], cmp)
		return sort(left, right, cmp)
		
L1= [x for x in range(10, 0, -1)]
L2 = [x for x in range(30, 0, -1)]
L3 = [x for x in range(100, 0, -1)]
print("L: {}\nL2: {}\L3: {}".format(L1, L2, L3))
merge_time_ten = time.perf_counter()
Sorted = mergeSort(L1, lambda l, r: l < r)
print("L sorted: {}".format(Sorted))
merge_time_ten = time.perf_counter() - merge_time_ten
merge_time_thirty = time.perf_counter()
Sorted2 = mergeSort(L2, lambda l, r: l < r)
print("L2 sorted: {}".format(Sorted2))
merge_time_thirty = time.perf_counter() - merge_time_thirty
merge_time_hundred = time.perf_counter()
Sorted3 = mergeSort(L3, lambda l, r: l < r)
print("L3 sorted: {}".format(Sorted3))
merge_time_hundred = time.perf_counter() - merge_time_hundred
# Charles Thomas Wallace Truscott Watters. Massachusetts Institute of Technology

def InsertionSort(L):
	t = time.perf_counter()
	for j in range(1, len(L)):
		key = L[j]
		i = j - 1
		while i >= 0 and L[i] > key:
			L[i + 1] = L[i]
			i -= 1
		L[i + 1] = key
	t2 = time.perf_counter() - t
	return L
L = [x for x in range(10, 0, -1)]
L2 = [x for x in range(30, 0, -1)]
L3 = [x for x in range(100, 0, -1)]
print("Unsorted List One: {}\nUnsorted List Two: {}\nUnsorted List Three {}".format(L, L2, L3))
ins_time_ten = time.perf_counter()
L = InsertionSort(L)
print("L sorted: {}".format(L))
ins_time_ten = time.perf_counter() - ins_time_ten
ins_time_thirty = time.perf_counter()
L2 = InsertionSort(L2)
print("L2 sorted: {}".format(L2))
ins_time_thirty = time.perf_counter() - ins_time_thirty
ins_time_hundred = time.perf_counter()
L3 = InsertionSort(L3)
print("L3 sorted: {}".format(L3))
ins_time_hundred = time.perf_counter() - ins_time_hundred
#print("The first took {} seconds and the second took {}".format(tl1, tl2))

print("Merge Sort, a log2 algorithm takes {} nanoseconds for a list of size ten and {} for a list of size thirty and {} for a list of size 100".format(merge_time_ten * 10 ** 5, merge_time_thirty * 10 ** 5, merge_time_hundred * 10 ** 5))

print("Insertion sort, an quadratic algorithm takes {} nanoseconds for a list of size ten and {} nanoseconds for a list of size thirty and {} nanoseconds for a list of size one hundred".format(ins_time_ten * 10 ** 5, ins_time_thirty * 10 ** 5, ins_time_hundred * 10 ** 5))
import numpy as np
print("Merge Sort, Ratios: a list of size ten {};  a list of size thirty {}; a list of size one hundred {}".format(((merge_time_ten * 10 ** 5) / np.log2(10)), ((merge_time_thirty * 10 ** 5) / np.log2(30)), ((merge_time_hundred * 10 ** 5) / np.log2(100))))

print("Insertion sort, Ratios: a list of size ten {}; a list of size thirty {}; a list of size one hundred {}".format((ins_time_ten * 10 ** 5) / 10 ** 2,  (ins_time_thirty * 10 ** 5) / 30 ** 2, (ins_time_hundred * 10 ** 5) / 100 ** 2))

"""

L: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L2: [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]\L3: [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
L3 sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
Unsorted List One: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Unsorted List Two: [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Unsorted List Three [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
L3 sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
Merge Sort, a log2 algorithm takes 3.5520999972504796 nanoseconds for a list of size ten and 8.500000012645614 for a list of size thirty and 19.99999999497959 for a list of size 100
Insertion sort, an quadratic algorithm takes 1.8229000033898046 nanoseconds for a list of size ten and 3.895800000464078 nanoseconds for a list of size thirty and 32.19270001864061 nanoseconds for a list of size one hundred
Merge Sort, Ratios: a list of size ten 1.0692886467703395;  a list of size thirty 1.7322579028464162; a list of size one hundred 3.010299955884165
Insertion sort, Ratios: a list of size ten 0.018229000033898046; a list of size thirty 0.004328666667182309; a list of size one hundred 0.0032192700018640608

[Program finished]

Charles Thomas Wallace Truscott Watters, MITx """