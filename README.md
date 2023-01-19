# Working Title: Predicting and Analyzing Greenhouse Gas Emissions

## Project Overview
As 2022 unfolded, a clear pathway of climate hope emerged. New policy breakthroughs have the potential to unlock enormous progress in the effort to slow and reverse warming temperatures. Encouraging developments from a very momentous year, as nation after nation elected more climate-oriented governments and enacted new efforts to curb greenhouse gas. in August the Biden administration and a narrow Democratic majority in Congress managed to pass the Inflation Reduction Act. 

This new U.S. law, backed by some $374 billion in climate spending, is the country's most aggressive piece of climate legislation ever. Its provisions ensure that for decades to come billions of dollars will roll toward the energy transition, making it easier to deploy renewable energy, build out green technologies and subsidize consumer adoption of everything from electric cars to heat pumps. Experts on energy modeling predict the law will eliminate 4 billion tons of greenhouse gas emissions.

For our project, we have an investor that would like to tap into the climate spending but doesn't know what sector or location to start. We will be utilizing the Climate Change Data from the World Bank for our database. It is data from World Development Indicators and Climate Change Knowledge Portal on climate systems, exposure to climate impacts, resilience, greenhouse gas emissions, and energy use. We will be using a machine learning model for predicting CO2 greenhouse gas emissions from economic growth indicatiors like Gross Domestic Product (GDP), population, and energy use per capita. We will be analyzing greenhouse gas emissions by the following:
- Trends/Factors: 
  - What are the countries’ annual CO2 emissions?
  - Per capita: how much CO2 does the average person emit?
  - How does GDP influence Co2 emissions? 
  - How does Urban population in a country affect CO2 emissions?
  - What share of global CO2 emissions are emitted by the country?
  - What are the countries’ annual CO2 emissions?
  - Cumulative: how much CO2 has it produced to date?
  - Year-on-year change: what is the percentage change in CO2 emissions?
- Machine Learning: 
  - Can a machine learning model show that there is a correlation between factors and emmisions?
- USA Data: 
  - Which state and city has the most emissions?
  - What sector does  

## Project Outline: Segment 3
- <b>Presentation: </b>
  - Content 
  - Google Slides
- <b>Github:</b>
  - Main Branch
  - README.md
  - Individual Branches
- <b>Machine Learning Model:</b>
  - Description of data preprocessing  
  - Description of feature engineering and the feature selection, including their decision-making process 
  - Description of how data was split into training and testing sets
  - Explanation of model choice, including limitations and benefits
  - Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)
  - Description of how they have trained the model thus far, and any additional training that will take place
  - Description of current accuracy score   
- <b>Dashboard:</b>
  - Images from the initial analysis
  - Data (images or report) from the machine learning task
  - At least one interactive element 

## Resources
- Data Source: [Climate Change Data | Data Catalog](https://datacatalog.worldbank.org/search/dataset/0040205), [Climate Watch](https://www.climatewatchdata.org/data-explorer/historical-emissions?historical-emissions-data-sources=climate-watch&historical-emissions-gases=all-ghg&historical-emissions-regions=All%20Selected&historical-emissions-sectors=total-including-lucf%2Ctotal-including-lucf&page=1), [Emissions by Unit and Fuel Type|US EPA](https://www.epa.gov/ghgreporting/data-sets), [countries.csv](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Resources/countries.csv), [ghg_emissions.csv](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Resources/ghg_emissions.csv), [USA_CO2_data.csv] (https://github.com/sahithig1/capstone_greenhouse_emissions/blob/presentation/Resources/USA_CO2_data.csv)
- Software: Jupyter Notebook 6.4.8, Python 3.7.13, Tableau Public 2022.3.0, MongoDB, Flask
- Library: Pandas, Matplotlib, Numpy, Seaborn, WBGAPI
- Overview Source: [Six climate breakthroughs that made 2022 a step toward net zero by Leslie Kaufman and Laura Millan Lombrana](https://www.stltoday.com/news/world/six-climate-breakthroughs-that-made-2022-a-step-toward-net-zero/article_b87f90e9-0945-56e9-ba52-0e1c053198eb.html), [United States: CO2 Country Profile by Hannah Ritchie and Max Roser](https://ourworldindata.org/co2/country/united-states?country=USA~CHN~JPN~DEU)

##  Results
### Machine Learning
#### Data preprocessing
- Unnecessary columns (like country)are dropped from the retrieved data.
- After ensuring there are no duplicates, the column headers of the dataset are renamed.
- Missing values per year are detected and years with a fair amount of data are considered for further analysis. The same logic is used to filter country data.
![](images/filter_shape.png?raw=true)
- The proportion of the missing data for each variable in the data is computed and the stacked bar plot is shown below:
![](images/missing_values.png?raw=true)
- Since dropping rows with nulls at this point drastically reduces the size and diversity of dataset, imputation of data is considered.
- Most of the data columns have skewed distribution. To refrain from introducing bias, the nulls are filled with respective median values.
- The rest of rows with null values are dropped from the dataset. The data is then inserted into the local Postgres database.
![](images/emissions_shape.png?raw=true)
- The model reads data from the database into a Pandas data frame.
- The model tests the hypothesis whether CO2 emissions depend on country-specific features (such as energy use, population metrics, GDP, cereal yield, etc. ) available in the dataset and can be predicted from these.
- The dataset has three dependent	variables that predict emissions.
- Upon plotting correlation matrix, emissions_per_capita is chose as label as this is correlated to many independent variables.
- The data is then checked for skewness and the distribution of data is visualized.
![](images/viz1.png?raw=true)
- As an attempt to address skewness in data, data is binned per dominant features and log transformation is used on all dependent and independent variables.
![](images/log1.png?raw=true)
- It is observed that the skew has reduced in the data distribution. Though not all features are fairly symmetric.
- Correlation matrix plotted after handling skewness showed increase in relation coefficients compared to original data. My dominant features are the 
- The Label and features are then determined.
![](images/sel1.png?raw=true)
![](images/sel2.png?raw=true)
- The training and testing data are split in 80:20 ratio.
- The DecisionTreeRegressor seems to handle skewness of data better.
- Since there are multiple independent variables that may predict emissions, a **Correlation** matrix is generated to reduce and interpret data.
- **CO<sub>2</sub> emissions_per_capita is considered target variable** as this is correlated to several predicting variables.
- A correlation value of 0.5 is set as threshold to select the features: Energy use per capita, GDP per capita, GNI per capita, Urban Population %, Electricity Access %, Cereal Yield 
- Later, each selected feature is visualized with the target variable. CO<sub>2</sub> emissions per capita shows a strong linear dependency to Energy use per capita and non-linear relationships with rest of the features.
- Since majority of features exhibit non-linear relationship with target variable, DecisionTreeRegressor and RandomForestRegressor models are chosen to predict emissions.
#### Current Accuracy Score


## Link to the Dashboard
[*pending* Link to the Dashboard](https://docs.google.com/presentation/d/e/2PACX-1vQYeBjycmIYUKQa_ksDCIQnI52Y7CwyaJ-3uvWlL2VfVYsqG3tEvpaX_F9x2d-6WKNKBScHEkWdv8hK/pub?start=false&loop=false&delayms=3000)

[Link to the Excel Dashboard Blueprint](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Visualization%20Tracker.xlsx)

[Link to Tableau dashboard](https://public.tableau.com/app/profile/soumya.abraham)

## Dashboard

In the Excel Dashboard Blueprint, you will find the following:
- Description of the tools used for the final dashboard
- Description of the interactive element
- Analysis for the visualizations
- Future visualization ideas and recommendations for improving current visualization

### Tableau
- We have opted for a blend of Plotly and Tableau in order to build an interactive website with informative data and accompanying visuals. 
- We also used various forms of filtering (by Year, Top 10 countries ect) to allow for a more comprehensive study of the charts provided.
- We used the Actions option in Tableau Dashboard, to include interactive selection and filtering elements to our visualization.
![actions](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Creating%20actions.png)

Through our dashboard, we will be able to dive into some visualizations to help our investors grasp the concepts of Green House Gas emissions and their effects on the environment. 

### Plotly:
-
### Machine Learning
-

#### Analysis 
At first glance, we can see that TX is the largest CO2 emitter in the country, followed by LA. 
When we click on the TX bar in the bar graph, we can see how these emissions are spread out over the various sectors. Chemicals sector is the highest contributor.
![TX1](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Statewise_Emissions_TX.png)

We also notice the the Chemical sector is the highest contributing sector for CO2 emission in LA. 
![LA1](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Statewise_Emissions_LA.png)

As the first step to our analysis, we can assume that Texas and Louisiana are high on our priority list of states needing assistance in cutting down their CO2 emissions, especially in the Chemicals sector.
![TX2](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Analysis_state_sector_TX.png)
![LA2](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Dashboard%20Images/Analysis_state_sector_LA.png)

We may need to look into the companies that emit the highest amounts of CO2 and see if they would be a good match for this investment goal.

## Link to the Presentation
[link to Google Slides Presentation](https://docs.google.com/presentation/d/e/2PACX-1vS_3j0Or_IGgdZwBIAsJDioPNrLeFdTmpARP94NagTTQFHqumSYEkyejG5D58UHU30W4D99TDhUWuLx/pub?start=false&loop=false&delayms=3000)

## Summary and Recommendations for the Dashboard



