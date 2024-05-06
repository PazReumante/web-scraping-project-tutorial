import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#DOWNLOAD HTML
url = "https://es.wikipedia.org/wiki/Leucocito"
html_data = requests.get(url, time.sleep(2)).text
html_data

#TRANFORM HTML
soup = BeautifulSoup(html_data)
html_table = soup.find("table",{"class":"wikitable"})
html_table

#FINDING THE TABLES
for row_index, row in enumerate(html_table.tbody.find_all('tr')):
   print(row_index, row)

#BUILDING THE DATA FRAME

arr_data = []

for row_index, row in enumerate(html_table.tbody.find_all('tr')):
   arr_cells_data = []
   if row_index == 0:
      for cell in row.find_all('th'):
         arr_cells_data.append(cell.get_text(strip=True))
   else:
      for cell in row.find_all('td'):
         arr_cells_data.append(cell.get_text(strip=True))
   
   arr_data.append(arr_cells_data)

arr_data

#SELECTING THE DATA BASE

df = pd.DataFrame(arr_data[1:], columns=arr_data[:1])
df
data_selection = df[['Tipo','Porcentaje aproximado en adultos']]
data_selection

#CREATING THE GRAPHS TO DISPLAY AND ANALYSE THE DATA

# Creating the DataFrame
df = pd.DataFrame(arr_data[1:], columns=arr_data[0])

# Selecting the desired columns
data_selection = df[['Tipo', 'Porcentaje aproximado en adultos']]

# Removing percentage symbols and converting to numeric
data_selection['Porcentaje aproximado en adultos'] = data_selection['Porcentaje aproximado en adultos'].str.rstrip('%').astype(float)

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: Bar plot
axes[0].bar(data_selection['Tipo'], data_selection['Porcentaje aproximado en adultos'])
axes[0].set_xlabel('Tipo')
axes[0].set_ylabel('Porcentaje aproximado en adultos')
axes[0].set_title('Leucocyte analysis nº 1')

# Plot 2: Scatter plot
axes[1].scatter(data_selection['Tipo'], data_selection['Porcentaje aproximado en adultos'])
axes[1].set_xlabel('Tipo')
axes[1].set_ylabel('Porcentaje aproximado en adultos')
axes[1].set_title('Leucocyte analysis nº 2')

# Plot 3: Line plot
axes[2].plot(data_selection['Tipo'], data_selection['Porcentaje aproximado en adultos'])
axes[2].set_xlabel('Tipo')
axes[2].set_ylabel('Porcentaje aproximado en adultos')
axes[2].set_title('Leucocyte analysis nº 3')

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()