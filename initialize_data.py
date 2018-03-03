# This file creates all the features of immunotherapy from
# the .csv data file. Splitting the features into individual
# objects will make accessing their values later on easier

import pandas as pd

# Create features sex, age, time, number of warts, type,
# area, induration diameter, and result of treatment
data = pd.read_csv("Immunotherapy.csv")

# Create 2D list with all labels
all_labels = []

sex = data["sex"]
del data["sex"]
all_labels.append(sex)

age = data["age"]
del data["age"]
all_labels.append(age)

time = data["Time"]
del data["Time"]
all_labels.append(time)

number_of_warts = data["Number_of_Warts"]
del data["Number_of_Warts"]
all_labels.append(number_of_warts)

type = data["Type"]
del data["Type"]
all_labels.append(type)

area = data["Area"]
del data["Area"]
all_labels.append(area)

induration_diameter = data["induration_diameter"]
del data["induration_diameter"]
all_labels.append(induration_diameter)

result_of_treatment = data["Result_of_Treatment"]
del data["Result_of_Treatment"]
all_labels.append(result_of_treatment)

# For use in other files
number_of_features = len(all_labels)
number_of_data = len(all_labels[0])

# Create training and testing set of data
training_labels = []
testing_labels = []
for i in range(number_of_features):
    training_labels.append(all_labels[i][:int(number_of_data/2)])
    testing_labels.append(all_labels[i][int(number_of_data/2):])