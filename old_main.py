from wisc_rapport_builder import Builder

if __name__ == "__main__":
	input_file_name = input("write name of excel-file: ")
	input_path = input_file_name + '.xlsx'
	rapport_builder = Builder(input_path)
	rapport_builder.build_rapport(input_file_name)
	print('Rapport generated succesfully!')