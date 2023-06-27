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
		builder_test = Builder('some_path')
		actual = builder_test.get_result(pd.read_excel('example_sheet.xlsx'))
		expected = [{'mål': 'VFI', 'score': 68, '95%ki': '63-80', 'percentil': 2}, {'mål': 'VSI', 'score': 86, '95%ki': '79-96', 'percentil': 18}, {'mål': 'RSI', 'score': 67, '95%ki': '62-77', 'percentil': 1}, {'mål': 'AHI', 'score': 82, '95%ki': '76-91', 'percentil': 12}, {'mål': 'FHI', 'score': 89, '95%ki': '81-99', 'percentil': 23}, {'mål': 'HIK', 'score': 70, '95%ki': '65-78', 'percentil': 2}]

		self.assertEqual(expected, actual)

	def test_get_recommendations_lav_HIK(self):
		builder_test = Builder('some_path')
		result_dict = [{'mål': 'VFI', 'score': 100, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 86, '95%ki': '70-90', 'percentil': 25}, {'mål': 'RSI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}, {'mål': 'HIK', 'score': 75, '95%ki': '145-151', 'percentil': 99}]
		actual = builder_test.get_recommendations(result_dict)
		expected = ['']
		self.assertEqual(expected, actual)
	
	def test_get_recommendations_two_recommendations(self):
		builder_test = Builder('some_path')
		result_dict = [{'mål': 'VFI', 'score': 84, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 80, '95%ki': '70-90', 'percentil': 25}, {'mål': 'RSI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}, {'mål': 'HIK', 'score': 90, '95%ki': '145-151', 'percentil': 99}]
		actual = builder_test.get_recommendations(result_dict)
		expected = ["""Verbal forståelse indebærer at kunne forklare betydningen af ord, samt at kunne forklare abstrakte sammenhænge imellem ord.
Når man scorer lavt på VFI, vil man ofte have svært ved det sproglige (både skriftligt og mundtligt) - samt at forstå og følge verbal instruktion.
Derfor kan det hjælpe at supplere med visuel afbildning af strukturen i hverdagen og løsningen af opgaver (både ift. lektier og i undervisningen) fx form af piktogrammer, ugeskemaer. \n""",
"""Arbejdshukommelse er udtryk for hvor meget mental "plads" man har at arbejde på. 
Hvis arbejdshukommelsen har lav kapacitet kan det derfor være svært at løse komplekse opgaver, som består af mange dele, 
som samtidigt skal anvendes - da der ikke er plads til at holde dem alle i sindet på samme tid.
Man kan sammenligne det med at have et mindre skrivebord at arbejde på. 
Så længe antallet af elementer ikke overstiger skrivebordets kapacitet behøver der ikke være udfordringer.
Mere komplekse opgaver kræver dog mere plads på skrivebordet!
Det vil ligeledes være udfordrende at modtage komplekse instrukser verbalt, da de tit stiller store krav til, at man kan bearbejde mange ord på en gang.
Derfor kan det hjælpe at "eksternalisere" beskeder, instruktioner og opgaver - både i klasseværelset og fx ifbm. lektier.
Dette kan tage form af skriftlige instrukser, piktogrammer, tegninger eller andre visuelle hjælpemidler.
Det kan også være konstruktivt at hjælpe eleven.
Disse visuelle hjælpemidler vil have til fælles, at de giver mulighed for, at man kan vende tilbage til en information, hvis man "taber" et element under den mentale bearbejdning.\n"""]
		#self.assertEqual(expected, actual)

	def test_get_comparison_to_mean(self):
		builder_test = Builder('some_path')
		test_score = 69
		expected = 'langt under gennemsnittet'
		actual = builder_test.get_comparison_to_mean(test_score)
		self.assertEqual(expected, actual)
		test_score = 75
		expected = 'noget under gennemsnittet'
		actual = builder_test.get_comparison_to_mean(test_score)
		self.assertEqual(expected, actual)
		test_score = 88
		expected = 'gennemsnitligt'
		actual = builder_test.get_comparison_to_mean(test_score)
		self.assertEqual(expected, actual)
		test_score = 116
		expected = 'noget over gennemsnittet'
		actual = builder_test.get_comparison_to_mean(test_score)
		self.assertEqual(expected, actual)
		test_score = 131
		expected = 'langt over gennemsnittet'
		actual = builder_test.get_comparison_to_mean(test_score)
		self.assertEqual(expected, actual)


	def test_create_description_of_scores(self):
		builder_test = Builder('some_path')
		result_dict = [{'mål': 'HIK', 'score': 75, '95%ki': '145-151', 'percentil': 99, }, {'mål': 'VFI', 'score': 100, '95%ki': '95-105', 'percentil': 50}, {'mål': 'VSI', 'score': 86, '95%ki': '70-90', 'percentil': 25}, {'mål': 'RSI', 'score': 86, '95%ki': '65-78', 'percentil': 4}, {'mål': 'AHI', 'score': 116, '95%ki': '110-130', 'percentil': 64}, {'mål': 'FHI', 'score': 130, '95%ki': '125-135', 'percentil': 94}]
		actual = builder_test.create_description_of_scores(result_dict)
		expected = 'HIK (hele skalaen intelligenskvotient) blev målt til 75 (95% KI mellem 145-151), hvilket er noget under gennemsnittet. Denne score var 99. percentil, hvilket vil sige at 99% af børnene i norm-gruppen scorede lavere. VFI (verbalt forståelses-indeks) blev målt til 100 (95% KI mellem 95-105), hvilket er gennemsnitligt. Denne score var 50. percentil, hvilket vil sige at 50% af børnene i norm-gruppen scorede lavere. VSI (visuo-spatial (visuelt/rumligt) indeks) blev målt til 86 (95% KI mellem 70-90), hvilket er gennemsnitligt. Denne score var 25. percentil, hvilket vil sige at 25% af børnene i norm-gruppen scorede lavere. RSI (logisk ræsonnerings-indeks) blev målt til 86 (95% KI mellem 65-78), hvilket er gennemsnitligt. Denne score var 4. percentil, hvilket vil sige at 4% af børnene i norm-gruppen scorede lavere. AHI (arbejdshukommelses-indeks) blev målt til 116 (95% KI mellem 110-130), hvilket er noget over gennemsnittet. Denne score var 64. percentil, hvilket vil sige at 64% af børnene i norm-gruppen scorede lavere. FHI (forarbejdningshastigheds-indeks) blev målt til 130 (95% KI mellem 125-135), hvilket er None. Denne score var 94. percentil, hvilket vil sige at 94% af børnene i norm-gruppen scorede lavere. '
		#self.assertEqual(expected, actual)
	

	def test_build_rapport(self):
		builder_test = Builder('example_sheet.xlsx')
		# will fail, if it fails to build
		builder_test.build_rapport()

		



if __name__ == '__main__':
	unittest.main()