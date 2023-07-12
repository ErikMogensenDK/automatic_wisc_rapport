from wisc_rapport_builder import *
from datetime import datetime

def gen_rapport():
	builder = Builder('excel_with_scores.xlsx')
	document = builder.build_rapport((f'WISC-IV_rapport_{datetime.today().strftime("%d-%m-%y")}', 0))
	return document

if __name__ == "__main__":
	gen_rapport()
