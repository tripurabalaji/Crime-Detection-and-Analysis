from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd 
import sys 
import numpy as np
import csv as csv

import xlwt
from pandas import ExcelWriter
from pandas import ExcelFile


# Data Cleaning and preparing

#Preparing Crime Data

df = pd.read_csv("crime.csv")
crime = df.ix[ 1:5 , ["INCIDENT_TYPE_DESCRIPTION","Location","Year"]]

mask = crime.Location != "(0E-8, 0E-8)"
crime = crime[mask]

from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
geolocator = Nominatim()

def getZipforLocation(x):
    try:
        location = geolocator.reverse(x).raw['address']             
        return int(float(location['postcode']))
    except:
        return 0
    return 0

crime['Zip'] = crime['Location'].apply(lambda x: getZipforLocation(x.replace("(","").replace(")","").strip()))
mask = crime['Zip'] != 0
crime = crime[mask]

print(crime)
print(crime.dtypes)

#Crime data Ready

#Preparing Restaurant Data                                       

dfr = pd.read_csv("crimedata.csv")
rest = dfr.ix[ : ,["BusinessName","Zip","LicenseAddDtTm"]]

mask = pd.notnull(rest['LicenseAddDtTm'])
rest = rest[mask]

from datetime import datetime
rest['LicYear'] = rest['LicenseAddDtTm'].apply(lambda x: float(datetime.strptime(x, '%m/%d/%Y %H:%M').year))

print(rest)
print(rest.dtypes)

# Restaurant Data Ready

# Data Analysis

result = pd.merge(rest, crime, on='Zip', how='left')

mask =  (pd.isnull(result.Year)) | (result.LicYear <= result.Year)
result = result[mask]
a = DataFrame({'DangerLevel' : result.groupby( [ "BusinessName", "Zip"] )['INCIDENT_TYPE_DESCRIPTION'].count()}).reset_index()
print(a)
print(type(a))

# Data Ready

# Printing to JSON File

a.to_json("analysis1.json")

#Plotting diagram

plt.figure(); a.plot(x='BusinessName', y='DangerLevel');

    


  










   





