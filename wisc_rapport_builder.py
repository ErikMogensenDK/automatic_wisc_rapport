import pandas as pd
from texts.anbefalinger import lav_anbefaling_df, generelle_anbefalinger
from texts.general_intro import*
from docx import Document
from docx.shared import Inches
from datetime import datetime

class Builder:
	def __init__(self, path_to_excel):
		try:
			self.result_df = pd.read_excel(path_to_excel)
		except:
			self.result_df = ''

	def get_introduction(self):
		introduction = generel_intro
		return introduction
	
	def get_comparison_to_mean(self, score):
		if score < 70:
			return 'langt under gennemsnittet'
		if score > 70 and score < 85:
			return 'noget under gennemsnittet'
		if score > 84 and score < 115:
			return 'gennemsnitligt'
		if score > 114 and score <130:
			return 'noget over gennemsnittet'
		if score > 130: 
			return 'langt over gennemsnittet'
			

	def create_description_of_scores(self, result_dict):
		long_version_dict = {'VFI': 'verbalt forståelses-indeks', 
		       'HIK': 'hele skalaen intelligenskvotient', 
		       'VSI': 'visuo-spatial (visuelt/rumligt) indeks', 
		       'FHI': 'forarbejdningshastigheds-indeks', 
		       'AHI': 'arbejdshukommelses-indeks',
		       'LRI': 'logisk ræsonnerings-indeks'}

		description = ''
		for result in result_dict:
			comparison_to_mean = self.get_comparison_to_mean(result['score'])
			description = description + f'''{result['mål']} ({long_version_dict[result['mål']]}) blev målt til {result['score']} (95% KI mellem {result['95%ki']}), hvilket er {comparison_to_mean}. Denne score var {result['percentil']}. percentil, hvilket vil sige at {result['percentil']}% af børnene i norm-gruppen scorede lavere. '''
			#descriptions.append(description)
		return description
	
	def add_table_to_document(self, document, result_dict):
		table = document.add_table(rows=7, cols=5) 
		hdr_cells = table.rows[0].cells 
		hdr_cells[0].text = 'Indeks' 
		hdr_cells[1].text = 'Score' 
		hdr_cells[2].text = '95%KI' 
		hdr_cells[3].text = 'Percentil' 
		hdr_cells[4].text = 'Beskrivelse' 
		for item in result_dict: 
			row_cells = table.add_row().cells 
			row_cells[0].text = str(item['mål'])
			row_cells[1].text = str(item['score']) 
			row_cells[2].text = str(item['95%ki'])
			row_cells[3].text = str(item['percentil'])
			row_cells[4].text = self.get_comparison_to_mean(item['score'])
		return document

	def get_recommendations(self, result_dict):
		recommendations = []
		for result in result_dict:
			if result['score'] < 85:
				recommendation = lav_anbefaling_df.loc[result['mål']][0]
				recommendations.append(recommendation)
		return recommendations
	

						
		# TODO: def create_description of scores(self, scores):


	def get_result(self, result_df):
		indexes = ['VFI', 'VSI', 'LRI', 'AHI', 'FHI', 'HIK']
		filtered_df = result_df[result_df.iloc[:, 0].isin(indexes)]
		result = filtered_df.to_dict(orient='records')
		return result

	def get_recommendations_for_HIK(self, result):
		# tjek om HIK er under eller over 85 og indsæt evt. følgende
		if result[0]['score'] < 85:
			return fortsat_intro_til_lav_begavelse
		if result[0]['score'] > 115:
			return fortsat_intro_til_høj_begavelse



	def build_rapport(self):
		document = Document()
		document.add_heading(f'WISC-IV rapport {datetime.today().strftime("%d-%m-%y")}', 0)
		document.add_paragraph(generel_intro)
		document.add_heading('Testresultat', 1)
		result = self.get_result(self.result_df)
		document.add_paragraph(self.create_description_of_scores(result))

		document = self.add_table_to_document(document, result)

		document.add_heading('Klinisk Indtryk', 1)
		document.add_paragraph()


		document.add_heading('Anbefalinger', 1)
		document.add_paragraph(self.get_recommendations_for_HIK(result))
		document.add_paragraph(self.get_recommendations(result))
		document.add_paragraph(generelle_anbefalinger)
		document.save(f'WISC_IV_rapport.docx')
		return document


	#def create_description()
		
# Insert general description

# create df from excel
# for row 2-6 (or whatever) in excel: report each col from df


# Insert general recommendations
# create recommendations based on scores
# for each column containing scores, if score lower than 85: 
#	Insert recommendation based on category in row with score lower than 85

# Create summary?