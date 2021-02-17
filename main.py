# Acea Smart Water Analytics - Water Availability Prediction

import pandas as pd
import numpy as np

# Waterbody: Auser

Auser = pd.read_csv('Aquifer_Auser.csv')

#Cleaning NAs in the 

Auser.dropna(subset=['Depth_to_Groundwater_SAL'], inplace=True)


#Feature engineering

Auser.replace({"Temperature_Orentano": 0}, np.NaN, inplace=True)
Auser.replace({"Temperature_Monte_Serra": 0}, np.NaN, inplace=True)
Auser.replace({"Temperature_Ponte_a_Moriano": 0}, np.NaN, inplace=True)


# Setting variables to the model
y = Auser['Depth_to_Groundwater_SAL']
X = Auser.drop('Depth_to_Groundwater_SAL', axis=1)