import pandas as pd

class Builder:
	def __init__(self, table_path = 'example_excel.xml'):
		self.df = pd.read_excel(table_path)


	#def create_description()
		
# Insert general description

# create df from excel
# for row 2-6 (or whatever) in excel: report each col from df


# Insert general recommendations
# create recommendations based on scores
# for each column containing scores, if score lower than 85: 
#	Insert recommendation based on category in row with score lower than 85

# Create summary?