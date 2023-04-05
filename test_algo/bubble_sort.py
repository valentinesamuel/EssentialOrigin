import unittest

numbers = [99, 46, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubbleSort(array):

	if not isinstance(array, list):
		raise TypeError

	for idx1 in range(len(array)):
		for idx in range(0, len(array) - idx1 - 1):
			if array[idx] > array[idx + 1]:
				array[idx], array[idx + 1] = array[idx + 1], array[idx]
	return array


# bubbleSort(numbers)


class TestBubbleSort(unittest.TestCase):

	def test_bubbleSort(self):
		self.assertEqual(bubbleSort([2, 1, 5, 63, 87]), [1, 2, 5, 63, 87])

	def test_bubbleSort_non_array(self):
		with self.assertRaises(TypeError):
			bubbleSort('[2,1,5,63,87]')


if __name__ == '__main__':
	unittest.main()
