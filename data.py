import csv

def get_data(file_path):
	"""
	Reads a CSV file and returns a dictionary where the keys are the 'id' values from the file and the values are dictionaries containing the data from each row.

	:param file_path: A string representing the path to the CSV file.
	:type file_path: str

	:return: A dictionary where the keys are the 'id' values from the file and the values are dictionaries containing the data from each row.
	:rtype: dict
	"""
	data = {}
	with open(file_path, 'r') as file:
		reader = csv.DictReader(file)
		for i, row in enumerate(reader):
			data[i] = row
	return data