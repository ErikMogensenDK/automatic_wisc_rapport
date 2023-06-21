import pandas as pd
from texts.anbefalinger import lav_anbefaling_df

class Builder:
	#def __init__(self):

	def get_introduction(self):
		introduction = ''
		return introduction

	def create_description_of_scores(self, result_dict):
		long_version_dict = {'VFI': 'verbalt forståelses-indeks', 
		       'HIK': 'hele skalaen intelligenskvotient', 
		       'VSI': 'visuo-spatial (visuelt/rumligt) indeks', 
		       'FHI': 'forarbejdningshastigheds-indeks', 
		       'AHI': 'arbejdshukommelses-indeks',
		       'LRI': 'logisk ræsonnerings-indeks'}

		descriptions = []
		for result in result_dict:
			description = f'''{result['mål']} ({long_version_dict[result['mål']]}) blev målt til {result['score']} .'''									
			descriptions.append(description)
		return descriptions

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



	#def create_description()
		
# Insert general description

# create df from excel
# for row 2-6 (or whatever) in excel: report each col from df


# Insert general recommendations
# create recommendations based on scores
# for each column containing scores, if score lower than 85: 
#	Insert recommendation based on category in row with score lower than 85

# Create summary?