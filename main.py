from medical_insurance import InsuranceData
from data import get_data

data = get_data('insurance.csv')
insurance_data = InsuranceData(data)

print("\nUnique columns: ")
columns = insurance_data.get_columns()
print(columns)

print("\nRegions frequency: ")
most_frequent_region = insurance_data.column_frequency('region')
least_frequent_age = insurance_data.column_frequency('age', most_frequent=False)

print("\nAge statistics: ")
average_age = insurance_data.get_average('age')
age_standard_deviation = insurance_data.get_standard_deviation('age')
age_median = insurance_data.get_median('age')

print("\nFiltered data with 5 children: ")
five_children_age = insurance_data.column_frequency('age', condition=lambda x: x['children'] == '5')
average_age_five_children = insurance_data.get_average('age', condition=lambda x: x['children'] == '5')
age_standard_deviation = insurance_data.get_standard_deviation('age', condition=lambda x: x['children'] == '5')
age_median = insurance_data.get_median('age', condition=lambda x: x['children'] == '5')

print("\nFiltered data with no children: ")
five_children_age = insurance_data.column_frequency('age', condition=lambda x: x['children'] == '0')
average_age_five_children = insurance_data.get_average('age', condition=lambda x: x['children'] == '0')
age_standard_deviation = insurance_data.get_standard_deviation('age', condition=lambda x: x['children'] == '0')
age_median = insurance_data.get_median('age', condition=lambda x: x['children'] == '0')

print("\nCosts statistics: ")
costs_average = insurance_data.get_average('charges')
costs_standard_deviation = insurance_data.get_standard_deviation('charges')
max_cost = insurance_data.get_max('charges')
min_cost = insurance_data.get_min('charges')
costs_median = insurance_data.get_median('charges')

print("\nDifference in charges with smoker: ")
costs_smokers = insurance_data.get_average('charges', condition=lambda x: x['smoker'] == 'yes', print_result=False)
print(f"The average cost for smokers is {round(costs_smokers, 2)}")
costs_nonsmokers = insurance_data.get_average('charges', condition=lambda x: x['smoker'] == 'no', print_result=False)
print(f"The average cost for non-smokers is {round(costs_nonsmokers, 2)}")
difference = costs_smokers - costs_nonsmokers
print(f"The difference in costs is {round(difference, 2)}")