# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:18:47 2024

@author: NC4135
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from pandasql import sqldf
from scipy import optimize

def saveFig(path,fileName, fileType = '.pdf'):
    plt.savefig(path+fileName+'.png',bbox_inches = 'tight')
    plt.savefig(path+fileName+'.tif',bbox_inches = 'tight')    
    plt.savefig(path+fileName+fileType,bbox_inches = 'tight',dpi=450)
    
def myplot_frame(figSize=(4, 3)):
    'plot function parameters'
    fig = plt.figure(figsize=figSize)
    ax = fig.add_subplot(1, 1, 1)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-large')
    plt.rc('ytick', labelsize='x-large')

    return ax
    

path = "I:\\FM\\\RM\\RMC DNB\\Research\\Climate Scenarios\\"

excel_file = 'Economic Scenarios.xlsx'

# Load Scenario desctiptions
dataSetFull = pd.read_excel(excel_file)

# Now you can work with the DataFrame 'df' as needed
print(dataSetFull.head())  # Display the first few rows of the DataFrame


'GDP Physical'
df = dataSetFull[dataSetFull['Variable Short']=='GDP Physical']
columns_to_drop= ['Variable Short', 'Scenario', 'Model', 'Region','Variable', 'Unit']

df = df.drop(columns = columns_to_drop)
df.set_index('Scenario Long', inplace=True)

#Out[29]: (['DT', 'FW', 'CP', 'NDC', 'NZ 250', 'B2C'], dtype='object', name='Scenario Short')
lineStyles = ['-.', '-', ':', '-.', ':', ':']
colors = ['grey', 'red', 'green', 'black', 'grey', 'blue']

axs = myplot_frame()
ax = df.T.plot(style=lineStyles, color = colors, ax = axs)
ax.set_title('GDP, Physical Risk')
ax.legend(df.index)
saveFig(path,'GDP_physical')

'GDP Transition'
df = dataSetFull[dataSetFull['Variable Short']=='GDP Transition']
columns_to_drop= ['Variable Short', 'Scenario', 'Model', 'Region','Variable', 'Unit']
df = df.drop(columns = columns_to_drop)
df.set_index('Scenario Long', inplace=True)

#Out[29]: (['DT', 'FW', 'CP', 'NDC', 'NZ 250', 'B2C'], dtype='object', name='Scenario Short')
lineStyles = ['-.', '-', ':', '-.', ':', ':']
colors = ['grey', 'red', 'green', 'black', 'grey', 'blue']

axs = myplot_frame()
ax = df.T.plot(style=lineStyles, color = colors, ax = axs)
ax.set_title('GDP, Transition Risk')
ax.legend(df.index)
saveFig(path,'GDP_Transition')

'GDP Combined'
df = dataSetFull[dataSetFull['Variable Short']=='GDP Combined']
columns_to_drop= ['Variable Short', 'Scenario', 'Model', 'Region','Variable', 'Unit']
df = df.drop(columns = columns_to_drop)
df.set_index('Scenario Long', inplace=True)

#Out[29]: (['DT', 'FW', 'CP', 'NDC', 'NZ 250', 'B2C'], dtype='object', name='Scenario Short')
lineStyles = ['-.', '-', ':', '-.', ':', ':']
colors = ['grey', 'red', 'green', 'black', 'grey', 'blue']

axs = myplot_frame()
ax = df.T.plot(style=lineStyles, color = colors, ax = axs)
ax.set_title('GDP, Combined Risk')
ax.set_ylabel('(%)')
ax.legend(df.index)
saveFig(path,'GDP_TCombined')

'-------------------------'

excel_file = 'Physical Scenarios.xlsx'

dataSetFull = pd.read_excel(excel_file)

# Now you can work with the DataFrame 'df' as needed
print(dataSetFull.head())  # Display the first few rows of the DataFrame


'Carbon Price'
df = dataSetFull[dataSetFull['Variable Short']=='Carbon Price']
columns_to_drop= ['Variable Short', 'Scenario', 'Model', 'Region','Variable', 'Unit']
df = df.drop(columns = columns_to_drop)
df.set_index('Scenario Long', inplace=True)

#Out[29]: (['DT', 'FW', 'CP', 'NDC', 'NZ 250', 'B2C'], dtype='object', name='Scenario Short')
lineStyles = ['-.', '-', ':', '-.', ':', ':']
colors = ['grey', 'red', 'green', 'black', 'grey', 'blue']

axs = myplot_frame()
ax = df.T.plot(style=lineStyles, color = colors, ax =axs )
ax.set_title('Carbon Price')
ax.set_ylabel('US$2010/t CO2')
ax.legend(df.index)
saveFig(path,'carbonPrice')

'Emissions|CO2'
df = dataSetFull[dataSetFull['Variable Short']=='CO2 Emissions']
columns_to_drop= ['Variable Short', 'Scenario', 'Model', 'Region','Variable', 'Unit']
df = df.drop(columns = columns_to_drop)
df.set_index('Scenario Long', inplace=True)

#Out[29]: (['DT', 'FW', 'CP', 'NDC', 'NZ 250', 'B2C'], dtype='object', name='Scenario Short')
lineStyles = ['-.', '-', ':', '-.', ':', ':']
colors = ['grey', 'red', 'green', 'black', 'grey', 'blue']

axs = myplot_frame()
ax = df.T.plot(style=lineStyles, color = colors, ax = axs)
ax.set_title('CO2 Emissions')
ax.set_ylabel('Mt CO2/yr')
ax.legend(df.index)
saveFig(path,'CO2Emissions')

'GDP Combined'
df = dataSetFull[dataSetFull['Variable Short']=='Median World Temperature']
columns_to_drop= ['Variable Short', 'Scenario', 'Model', 'Region','Variable', 'Unit']
df = df.drop(columns = columns_to_drop)
df.set_index('Scenario Long', inplace=True)

#Out[29]: (['DT', 'FW', 'CP', 'NDC', 'NZ 250', 'B2C'], dtype='object', name='Scenario Short')
lineStyles = ['-.', '-', ':', '-.', ':', ':']
colors = ['grey', 'red', 'green', 'black', 'grey', 'blue']

axs = myplot_frame()
ax = df.T.plot(style=lineStyles, color = colors, ax = axs)
ax.set_title('Median World Temperature')
ax.set_ylabel('Degrees')
ax.legend(df.index)
saveFig(path,'MedianWorldTemperature')


'''
df = sqldf(query, locals())
query = """
        SELECT *
        FROM dataSetFull
        WHERE Region = 'NiGEM NGFS v1.23.2|United States'
        AND Model = 'NiGEM NGFS v1.23.2[GCAM 6.0 NGFS]' 
        AND ( Variable = 'Unemployment rate ; %(combined)' OR Variable = 'Long term real interest rate ; %')        

        """


        AND Variable = 'Long term real interest rate ; \%'
'''