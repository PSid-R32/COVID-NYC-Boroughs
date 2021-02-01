import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def absval(value):
  whole  = np.round(value/100.*c19_deaths.sum(), 0)
  return whole

df = pd.read_csv('deaths.csv')
boro = df['BOROUGH_GROUP']
c19_deaths = df['DEATH_COUNT']
plt.pie(c19_deaths, labels=boro, autopct=absval, shadow=True, startangle=90)
plt.title('COVID-19 Deaths by NYC Borough', fontsize=24)
plt.show()
