import unittest
#from .automatic_wisc_repport import wisc_repport_builder
from automatic_wisc_repport.wisc_repport_builder import Builder
import pandas as pd


class TestExplainerMethods(unittest.TestCase):
	def test_create_df_of_scores(self):
		builder_test = Builder('example_excel.xml')
		# create dataframe = example_excel
		df = pd.read_excel(example_table_path)

		# assert that df's are equal?
		# asser that individual fields of the df are equal?
		expected = '100'
		# insert correct indexing into df
		result = df('score', 'VFI')
		self.assertEqual()

if __name__ == '__main__':
	unittest.main()