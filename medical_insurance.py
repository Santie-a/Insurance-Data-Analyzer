class InsuranceData:
	def __init__(self, data):
		self.data = data
	def column_frequency(self, column_name: str, most_frequent: bool = True, condition = lambda x: x) -> dict:
		"""
		Calculates the frequency of values in a specified column of the data dictionary.

		Parameters:
		    column_name (str): The name of the column to calculate the frequency for.
		    most_frequent (bool, optional): If True, returns the most frequent value and its frequency. If False, returns the least frequent value and its frequency. Defaults to True.
		    condition (function, optional): A lambda function that specifies a condition for filtering the data. Defaults to lambda x: x.

		Returns:
		    dict: A dictionary containing the frequency of each unique value in the specified column. If most_frequent is True, returns the most frequent value and its frequency. If most_frequent is False, returns the least frequent value and its frequency.
		"""
		data = {k: v for k, v in self.data.items() if condition(v)}
		different_values = dict()
		try:
			for record in data:
				value = data[record][column_name]

				if value not in different_values:
					different_values[value] = 1
				else:
					different_values[value] += 1

			if most_frequent:
				max_key = max(different_values, key=different_values.get)
				print(f"The most frequent value for {column_name} is {max_key} with {different_values[max_key]} record(s).")

				return different_values[max_key]
			else:
				min_key = min(different_values, key=different_values.get)
				print(f"The least frequent value for {column_name} is {min_key} with {different_values[min_key]} record(s).")

				return different_values[min_key]
		
		except Exception as e:
			print(f"Error: {e}")
			return {}
		
	def get_columns(self):
		"""
		Returns a list of all unique columns in the data dictionary.

		:return: A list of strings representing the unique columns in the data dictionary.
		:rtype: list
		"""
		columns = []
		
		for record in self.data:
			for column in self.data[record]:
				if column not in columns:
					columns.append(column)

		return columns
	
	def get_average(self, column_name: str, print_result: bool = True, condition = lambda x: x):
		"""
		Calculates the average value in a specified column of a dictionary.

		:param column_name: The name of the column to calculate the average value from.
		:type column_name: str
		:param print_result: If True, prints the average value. Defaults to True.
		:type print_result: bool
		:param condition: A lambda function that specifies a condition for filtering the data. Defaults to lambda x: x.
		:type condition: function
		:return: The average value in the specified column. If an error occurs, returns -1.
		:rtype: float
		"""
		data = {k: v for k, v in self.data.items() if condition(v)}
		try:
			total = 0
			count = 0
			for record in data:
				value = float(data[record][column_name])
				total += value
				count += 1
			average = total / count
			if print_result: print(f"The average value for {column_name} is {round(average, 2)}.")

			return average
		
		except Exception as e:
			print(f"Error: {e}")
			return -1
		
	def get_standard_deviation(self, column_name: str, condition = lambda x: x):
		"""
		Calculates the standard deviation in a specified column of a dictionary.

		:param column_name: The name of the column to calculate the standard deviation from.
		:type column_name: str
		:param condition: A lambda function that specifies a condition for filtering the data. Defaults to lambda x: x.
		:type condition: function
		:return: The standard deviation in the specified column. If an error occurs, returns -1.
		:rtype: float
		"""
		data = {k: v for k, v in self.data.items() if condition(v)}
		try:
			total = 0
			count = 0
			mean = self.get_average(column_name, print_result=False)
			for record in data:
				value = float(data[record][column_name])
				total += (value - mean) ** 2
				count += 1
			standard_deviation = (total / count) ** 0.5
			print(f"The standard deviation for {column_name} is {round(standard_deviation, 2)}.")

			return standard_deviation
		
		except Exception as e:
			print(f"Error: {e}")
			return -1

	def get_median(self, column_name: str, condition = lambda x: x):
		"""
		Calculates the median value in a specified column of a dictionary, after applying a condition.

		:param column_name: The name of the column to calculate the median value from.
		:type column_name: str
		:param condition: A lambda function that specifies a condition for filtering the data. Defaults to lambda x: x.
		:type condition: function
		:return: The median value in the specified column. If an error occurs, returns -1.
		:rtype: float
		"""

		data = {k: v for k, v in self.data.items() if condition(v)}
		try:
			values = []
			for record in data:
				value = float(data[record][column_name])
				values.append(value)

			values.sort()
			length = len(values)

			if length % 2 == 0:
				median = (values[length // 2] + values[length // 2 - 1]) / 2
			else:
				median = values[length // 2]

			print(f"The median value for {column_name} is {round(median, 2)}.")

			return median
		
		except Exception as e:
			print(f"Error: {e}")
			return -1
		

	def get_max(self, column_name: str, condition = lambda x: x):
		"""
		Calculates the maximum value in a specified column of a dictionary, after applying a condition.

		:param column_name: The name of the column to calculate the maximum value from.
		:type column_name: str
		:param condition: A lambda function that specifies a condition for filtering the data. Defaults to lambda x: x.
		:type condition: function
		:return: The maximum value in the specified column. If an error occurs, returns -1.
		:rtype: float
		"""
		data = {k: v for k, v in self.data.items() if condition(v)}
		try:
			values = []
			for record in data:
				value = float(data[record][column_name])
				values.append(value)

			maximum = max(values)
			print(f"The maximum value for {column_name} is {round(maximum, 2)}.")

			return maximum
		
		except Exception as e:
			print(f"Error: {e}")
			return -1
		

	def get_min(self, column_name: str, condition = lambda x: x):
		"""
		Calculates the minimum value in a specified column of a dictionary, after applying a condition.

		:param column_name: The name of the column to calculate the minimum value from.	
		:type column_name: str
		:param condition: A lambda function that specifies a condition for filtering the data. Defaults to lambda x: x.
		:type condition: function
		:return: The minimum value in the specified column. If an error occurs, returns -1.
		:rtype: float
		"""
		data = {k: v for k, v in self.data.items() if condition(v)}
		try:
			values = []
			for record in data:
				value = float(data[record][column_name])
				values.append(value)

			minimum = min(values)
			print(f"The minimum value for {column_name} is {round(minimum, 2)}.")

			return minimum
		
		except Exception as e:
			print(f"Error: {e}")
			return -1