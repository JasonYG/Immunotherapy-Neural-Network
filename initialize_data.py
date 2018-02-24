# This file creates all the features of immunotherapy from
# the .csv data file. Splitting the features into individual
# objects will make accessing their values later on easier

import pandas as pd

# Create features sex, age, time, number of warts, type, area,
# induration diameter, and result of treatment
data = pd.read_csv("Immunotherapy.csv")

sex = data["sex"]
del data["sex"]

age = data["age"]
del data["age"]

time = data["Time"]
del data["Time"]

number_of_warts = data["Number_of_Warts"]
del data["Number_of_Warts"]

type = data["Type"]
del data["Type"]

area = data["Area"]
del data["Area"]

induration_diameter = data["induration_diameter"]
del data["induration_diameter"]

result_of_treatment = data["Result_of_Treatment"]
del data["Result_of_Treatment"]