from data import get_data

data = get_data('insurance.csv')

def most_frequent_column(column_name: str, data: dict) -> str:
	for record in data:
		print(record[column_name])