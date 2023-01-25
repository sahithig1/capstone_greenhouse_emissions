#!/usr/bin/env python
# coding: utf-8

# ### This file holds the Flask app and navigation code for dashboard.

# In[1]:


# Import dependencies
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px


# In[2]:


# Initialize Flask app
app = Flask(__name__)


# In[3]:


# Function to get total amount of gas emissions
def load_gases():
    df = pd.read_csv(
        "https://emissions-bucket.s3.amazonaws.com/ghg_emissions_viz.csv")
    gas_dict = {'Gas': ['CO2', 'CH4', 'NO2'],
                'Emissions': [df['emissions_total'].sum(), df['methane_emissions(kt_CO2_emissions)'].sum(), df['nitrous_oxide_emissions(mt_CO2_emissions)'].sum()]}
    total_df = pd.DataFrame(gas_dict)
    return total_df


# In[4]:


# Home Page
@app.route('/')
def index():
    # Get and graph gases data
    gas_df = load_gases()
    # Create a pie chart with data and style parameters
    fig = px.pie(gas_df,
                 values='Emissions',
                 names='Gas',
                 color='Gas',
                 height=330,
                 width=550,
                 color_discrete_map={'CO2': '#CCCCCC',
                                     'CH4': '#F17C1E',
                                     'NO2': '#425EAC'})
    fig.update_traces(textposition='inside', textinfo='percent+label')

    # Convert figure to JSON format
    gasJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # Render template with JSON data
    return render_template('index.html', gasJSON=gasJSON)


# In[5]:


# Trends link on dashboard
@app.route('/trends')
def load_trends():
    return render_template('trends.html')


# In[6]:


# Route to navigate to Factors link
@app.route('/factors')
def load_factors():
    return render_template('factors.html')


# In[7]:


# Route to navigate to USA link
@app.route('/usdata')
def load_us_data():
    return render_template('us_data.html')


# In[8]:


# Load the Analysis link on dashboard
@app.route('/analysis')
def load_analysis():
    return render_template('analysis.html')


# In[ ]:
if __name__ == "__main__":
    app.run()
