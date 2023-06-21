import unittest
#from .automatic_wisc_rapport import wisc_rapport_builder
from wisc_rapport_builder import Builder
import pandas as pd


class TestBuilderMethods(unittest.TestCase):
#	def test_get_recommendations(self):
#		builder_test = Builder('example_excel.xlsx')
#
#		expected = 'Lav HIK.'
#		actual = builder_test.get_recommendations()
#		self.assertEqual(expected, actual)

	def test_get_result(self):
		builder_test = Builder()
		actual = builder_test.get_result(pd.read_excel('example_excel.xlsx'))
		expected = [{'mål': 'VFI', 'score': 100, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 86, '95%ki': '70-90', 'percentil': 25}, {'mål': 'LRI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}, {'mål': 'HIK', 'score': 75, '95%ki': '145-151', 'percentil': 99}]
		print(len(actual))
		self.assertEqual(expected, actual)


if __name__ == '__main__':
	unittest.main()