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
		expected = [{'mål': 'HIK', 'score': 75, '95%ki': '145-151', 'percentil': 99, }, {'mål': 'VFI', 'score': 100, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 86, '95%ki': '70-90', 'percentil': 25}, {'mål': 'LRI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}]
		self.assertEqual(expected, actual)

	def test_get_recommendations_lav_HIK(self):
		builder_test = Builder()
		result_dict = [{'mål': 'VFI', 'score': 100, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 86, '95%ki': '70-90', 'percentil': 25}, {'mål': 'LRI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}, {'mål': 'HIK', 'score': 75, '95%ki': '145-151', 'percentil': 99}]
		actual = builder_test.get_recommendations(result_dict)
		expected = ['Lav HIK.']
		self.assertEqual(expected, actual)

	def test_get_recommendations_two_recommendations(self):
		builder_test = Builder()
		result_dict = [{'mål': 'VFI', 'score': 84, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 80, '95%ki': '70-90', 'percentil': 25}, {'mål': 'LRI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}, {'mål': 'HIK', 'score': 90, '95%ki': '145-151', 'percentil': 99}]
		actual = builder_test.get_recommendations(result_dict)
		expected = ["""
Verbal forståelse indebærer at kunne forklare betydningen af ord, samt at kunne forklare abstrakte sammenhænge imellem ord.
Når man scorer lavt på VFI, vil man derfor ofte have svært ved sproglige fag - samt at forstå og følge verbal instruktion.
Derfor kan det hjælpe at supplere med visuel afbildning af strukturen i hverdagen og løsningen af opgaver (både ift. lektier og i undervisningen) fx form af piktogrammer, ugeskemaer. \n""",
"""Arbejdshukommelse er udtryk for hvor meget mental "plads" man har at arbejde på. 
Hvis arbejdshukommelsen har lav kapacitet kan det derfor være svært at løse komplekse opgaver som består af mange dele, 
som samtidigt skal anvendes - da der ikke er plads til at holde dem alle i sindet på samme tid.
Man kan sammenligne det med at have et mindre skrivebord at arbejde på. 
Så længe antallet af elementer ikke overstiger skrivebordets kapacitet behøver der ikke være udfordringer.
Mere komplekse opgaver kræver dog mere plads på skrivebordet!
Det vil ligeledes være udfordrende at modtage komplekse instrukser verbalt, da de tit stiller store krav til, at man kan bearbejde mange ord på en gang.
Derfor kan det hjælpe at "eksternalisere" beskeder, instruktioner og opgaver - både i klasseværelset og fx ifbm. lektier.
Dette kan tage form af skriftlige instrukser, piktogrammer, tegninger eller andre visuelle hjælpemidler.
Det kan også være konstruktivt at hjælpe eleven.
Disse visuelle hjælpemidler vil have til fælles, at de giver mulighed for, at man kan vende tilbage til en information, hvis man "taber" et element under den mentale bearbejdning.\n"""]
		self.assertEqual(expected, actual)

	def test_create_description_of_scores(self):
		builder_test = Builder()
		result_dict = [{'mål': 'HIK', 'score': 75, '95%ki': '145-151', 'percentil': 99, }, {'mål': 'VFI', 'score': 100, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 86, '95%ki': '70-90', 'percentil': 25}, {'mål': 'LRI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}]
		actual = builder_test.create_description_of_scores(result_dict)
		print(actual)
		expected = 'example_description'
		self.assertEqual(expected, actual)
		



if __name__ == '__main__':
	unittest.main()