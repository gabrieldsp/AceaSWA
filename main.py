# Acea Smart Water Analytics - Water Availability Prediction

import pandas as pd
import numpy as np

# Waterbody: Auser

Auser = pd.read_csv('Aquifer_Auser.csv')
Auser.dropna(subset=['Depth_to_Groundwater_SAL'], inplace=True)
y = Auser['Depth_to_Groundwater_SAL']
X = Auser.drop('Depth_to_Groundwater', axis='column')