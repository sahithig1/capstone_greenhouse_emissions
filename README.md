# Working Title: Predicting and Analyzing Greenhouse Gas Emmissions

## Project Overview
As 2022 unfolded, a clear pathway of climate hope emerged. New policy breakthroughs have the potential to unlock enormous progress in the effort to slow and reverse warming temperatures. Encouraging developments from a very momentous year, as nation after nation elected more climate-oriented governments and enacted new efforts to curb greenhouse gas. in August the Biden administration and a narrow Democratic majority in Congress managed to pass the Inflation Reduction Act. 

This new U.S. law, backed by some $374 billion in climate spending, is the country's most aggressive piece of climate legislation ever. Its provisions ensure that for decades to come billions of dollars will roll toward the energy transition, making it easier to deploy renewable energy, build out green technologies and subsidize consumer adoption of everything from electric cars to heat pumps. Experts on energy modeling predict the law will eliminate 4 billion tons of greenhouse gas emissions.

For our project, we have an investor that would like to tap into the climate spending but doesn't know what sector or location to start. We will be utilizing the Climate Change Data from the World Bank for our database. It is data from World Development Indicators and Climate Change Knowledge Portal on climate systems, exposure to climate impacts, resilience, greenhouse gas emissions, and energy use. We will be using a machine learning model for predicting CO2 greenhouse gas emissions from economic growth indicatiors like Gross Domestic Product (GDP), population, and energy use per capita. We will be analyzing greenhouse gas emissions by the following:
- Per capita: how much CO2 does the average person emit?
- What are the countries’ annual CO2 emissions?
- Year-on-year change: what is the percentage change in CO2 emissions?
- Cumulative: how much CO2 has it produced to date?
- What share of global CO2 emissions are emitted by the country?
- Total greenhouse gas emissions: how much does the average person emit? Where do emissions come from? 
- Does energy used to sustain a person in a country have an effect on CO2 emissions? 
- How does GDP influence Co2 emissions? 
- How does Urban population in a country affect CO2 emissions?

## Communication protocols
We are utilizing our Slack group project channel to relay information to each other. We have divided the project by presentation, GitHub, Machine Learning Model, Database and Dashboard. We created branches for each deliverable and will use that branch for our portion of the project. When we are ready for pull requests to be approved, we will indicate via Slack that we are ready for the person in charge of Github to act accordingly. We are meeting 2 times a week to collaborate and ensure we are answering each others' questions. 

## Project Outline: Segment 2
- <b>Presentation: </b>
  - Content 
  - Google Slides
- <b>Github:</b>
  - Main Branch
  - README.md
  - Individual Branches
- <b>Machine Learning Model:</b>
  - Preliminary data preprocessing 
  - Preliminary feature engineering
  - Preliminary feature selection
  - Decision-making process 
  - How data was split into training and testing sets
  - Model choice, including limitations and benefits
- <b>Database:</b>
  - Database stores static data for use during the project
  - database connects to the model
  - Includes at least two tables
  - Includes at least one join using the database language
  - Includes at least one connection string
  - ERD
- <b>Dashboard:</b>
  - Storyboard on Google Slides
  - Tools that will be used to create final dashboard 
  - Interactive elements 

## Resources
- Data Source: [Climate Change Data | Data Catalog](https://datacatalog.worldbank.org/search/dataset/0040205), [Climate Watch](https://www.climatewatchdata.org/data-explorer/historical-emissions?historical-emissions-data-sources=climate-watch&historical-emissions-gases=all-ghg&historical-emissions-regions=All%20Selected&historical-emissions-sectors=total-including-lucf%2Ctotal-including-lucf&page=1), [Emissions by Unit and Fuel Type|US EPA](https://www.epa.gov/ghgreporting/data-sets), [countries.csv](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Resources/countries.csv), [ghg_emissions.csv](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Resources/ghg_emissions.csv)
- Software: Jupyter Notebook 6.4.8, Python 3.7.13, Tableau Public 2022.3.0
- Library: WBGAPI, Pandas, Numpy
- Overview Source: [Six climate breakthroughs that made 2022 a step toward net zero by Leslie Kaufman and Laura Millan Lombrana](https://www.stltoday.com/news/world/six-climate-breakthroughs-that-made-2022-a-step-toward-net-zero/article_b87f90e9-0945-56e9-ba52-0e1c053198eb.html), [United States: CO2 Country Profile by Hannah Ritchie and Max Roser](https://ourworldindata.org/co2/country/united-states?country=USA~CHN~JPN~DEU)

##  Results
### Database
#### Data Collection  
We used a python library(wbgapi) that fetches World Bank Data directly into the dataframe using API. 

#### Data Cleaning and Analysis
- Pandas is used to clean the data and perform an exploratory analysis.
- Basic cleaning is done on the dataset to remove empty values.
- The data is then loaded into a local PostGres database.


#### Database Storage
Postgres(SQL) is the database we intend to use, and the structure of the database is designed using the QuickDBD tool. We will eventually run the database in AWS.

The ERD diagram is shown below,

![ERD diagram](images/ERD.png?raw=true)

* Database stores static data for use during the project.
![ghg_emissions](images/ghg_emissions_sample_data.png?raw=true)
![sector_emissions](images/sector_emissions_sample_data.png?raw=true)

* Database interfaces with the project in some format (database connects to the model)
![ML connected](images/MLconnected_db.png?raw=true)

#### Data Extraction:

- Datasets from [Climate TRACE](https://climatetrace.org/) are downloaded. After exploring the data, this dataset is not considered due to lack of dependent features that can address the project's outcome.
- Later, World Bank climate change data is downloaded to train the model. Though, there are several ways to retrieve the dataset, Python's wbgapi API is used due to the ease of data retrieval and availability of current data.

### Machine Learning
#### Emissions Model Creation:

- The data retrieved from the local PostGres database is considered as initial data set for the model. The dataset has 3552 rows and 19 columns.
<img src="images/emissions_df.png" width="300"/>

- With 19 columns to explore, the variables involved are classified as dependent and independent variables.
- Dependent Variables
  - emissions_total
  - emissions_per_capita
  - emissions_per_gdp
- Variables to drop: year, country_name, country_code
- The rest are considered as independent variables.

<img src="images/filter_shape.png" width="300"/>

<img src="images/emissions_shape.png" width="300"/>

<img src="images/missing_values.png" width="300"/>

<img src="images/raw_shape.png" width="300"/>

## Link to the Dashboard
[Link to the Google Slides Blueprint](https://docs.google.com/presentation/d/e/2PACX-1vQYeBjycmIYUKQa_ksDCIQnI52Y7CwyaJ-3uvWlL2VfVYsqG3tEvpaX_F9x2d-6WKNKBScHEkWdv8hK/pub?start=false&loop=false&delayms=3000)

[Link to Tableau dashboard](https://public.tableau.com/app/profile/soumya.abraham)

For our dashboard visualizations, we have primarily opted for Tableau Public.
After bringing in our csv files, we chose various forms of graphs and maps to show the relationship between CO2 emissions and various factors such as GDP per capita, emissions per GDP, population growth etc. 
- We also used various forms of filtering (by Year, Top 10 countries ect) to allow for a more comprehensive stufy of the charts provided. 
- We used the Actions option in Tableau Dashboard, to include interactive selection and filtering elements to our visualization.

![Dashboard Actions]<img src="https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Creating%20actions.png" width="600"/>

In the Google Slides Blueprint, you will find the following:
- Description of the tools used for the final dashboard
- Description of the interactive element
- Analysis for the visualizations
- Next steps to take for Segment 3
- Future visualization ideas and recommendations for improving current visualization

In the Tableau dashboard, you will find initial visualizations. Examples of visualization include the following:

![Emissions per GDP vs CO2 Emission]<img src="https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Emissions%20per%20GDP%20vs%20CO2%20Emission.png" width="600"/>

![Emissions per Capita]<img src="https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Emissions%20per%20Capita.png" width="600"/>

![Energy consumption per Capita vs Emissions]<img src="https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Energy%20consumption%20per%20Capita%20vs%20Emissions.png" width="600"/>



## Link to the Presentation
[link to Google Slides Presentation](https://docs.google.com/presentation/d/e/2PACX-1vS_3j0Or_IGgdZwBIAsJDioPNrLeFdTmpARP94NagTTQFHqumSYEkyejG5D58UHU30W4D99TDhUWuLx/pub?start=false&loop=false&delayms=3000)

## Summary and Recommendations
### Exploratory Data Analysis Summary
- Since there are multiple independent variables that may predict emissions, a **Correlation** matrix is generated to reduce and interpret data.
- **CO<sub>2</sub> emissions_per_capita is considered target variable** as this is correlated to several predicting variables.
- A correlation value of 0.5 is set as threshold to select the features: Energy use per capita, GDP per capita, GNI per capita, Urban Population %, Electricity Access %, Cereal Yield 
- Later, each selected feature is visualized with the target variable. CO<sub>2</sub> emissions per capita shows a strong linear dependency to Energy use per capita and non-linear relationships with rest of the features.
- Since majority of features exhibit non-linear relationship with target variable, DecisionTreeRegressor and RandomForestRegressor models are chosen to predict emissions.
