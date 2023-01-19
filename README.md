# Working Title: Predicting and Analyzing Greenhouse Gas Emissions

## Project Overview
As 2022 unfolded, a clear pathway of climate hope emerged. New policy breakthroughs have the potential to unlock enormous progress in the effort to slow and reverse warming temperatures. Encouraging developments from a very momentous year, as nation after nation elected more climate-oriented governments and enacted new efforts to curb greenhouse gas. in August the Biden administration and a narrow Democratic majority in Congress managed to pass the Inflation Reduction Act. 

This new U.S. law, backed by some $374 billion in climate spending, is the country's most aggressive piece of climate legislation ever. Its provisions ensure that for decades to come billions of dollars will roll toward the energy transition, making it easier to deploy renewable energy, build out green technologies and subsidize consumer adoption of everything from electric cars to heat pumps. Experts on energy modeling predict the law will eliminate 4 billion tons of greenhouse gas emissions.

For our project, we have an investor that would like to tap into the climate spending but doesn't know what sector or location to start. We will be utilizing the Climate Change Data from the World Bank for our database. It is data from World Development Indicators and Climate Change Knowledge Portal on climate systems, exposure to climate impacts, resilience, greenhouse gas emissions, and energy use. We will be using a machine learning model for predicting CO2 greenhouse gas emissions from economic growth indicatiors like Gross Domestic Product (GDP), population, and energy use per capita. We will be analyzing greenhouse gas emissions by the following:

- General
  - What countries have the largest CO2 greenhouse gas emissions (GHG)?
  - What are the GHG emissions per country?
- Machine Learning: 
  - Can a machine learning model show that there is a correlation between factors that may influence CO2 emissions?
- Factors influencing emissions: 
  - How does CO2 emissions change year over year?
  - How does GDP influence CO2 emissions? 
  - How does population influence CO2 emissions? 
- USA Data: 
  - Which state and city has the most CO2 emissions?
  - What sector generates the most CO2 emissions?
  - What cities contribute to the CO2 emissions' sectors?

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
### Database
We used a python library(wbgapi) that fetches World Bank Data directly into the dataframe using API. Pandas is used to clean the data and perform an exploratory analysis. The data is then loaded into a local PostGres database. Postgres(SQL) is the database we intend to use, and the structure of the database is designed using the QuickDBD tool. We will eventually run the database in AWS.

#### The ERD diagram is shown below,

![ERD diagram](images/ERD_final.png?raw=true)

#### Database stores static data for use during the project.

![ghg_emissions](images/ghg_emissions_sample.png?raw=true)
![sector_emissions](images/sector_emissions_sample.png?raw=true)

#### Join using the database language

![sql_join_ghg_emissions](images/sql_join_ghg_emissions.png?raw=true)
![sql_join_sector_emissions](images/sql_join_sector_emissions.png?raw=true)

#### Database interfaces with the project in some format (database connects to the model)
![ML connected](images/MLconnected_db.png?raw=true)

#### Data Extraction:
- The data for the project is extracted from the World bank database. Though, there are several ways to retrieve the dataset, Python’s WBGAPI is chosen because of the ease of data retrieval and availability of current data.
![](images/raw_shape.png?raw=true)

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
[Link to the Heroku Dashboard](https://ghflask.herokuapp.com/)

[Link to the Excel Dashboard Blueprint](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/Visualization/Visualization%20Tracker.xlsx)

## Dashboard
In the Heroku Dashboard, you will find the following:
- The web application has a header image and navigation bar with several tabs. Upon clicking the navigation links, the user is directed to visual analysis.
- The Home tab gives an overview of Greenhouse Gases and their emissions with various visuals to help grasp concepts better.  
- The Model will summarize the prediction of Machine Learning algorithms used in the project.
- The Factors tab employs interactivity with radio buttons that allow selection of a factor that can influence emissions.
- The USA tab dives into the CO2 emissions within the country. 
	- We have a map on the left showcasing the CO2 emissions within each city and state. A dropdown filter allows you to choose specific cities the investor may be interested in. This can be useful when you want to declutter the map to provide emissions in specific state(s).
	- The bar graph on the right shows the CO2 emissions per state, sorted in descending order. You will notice that Texas has the highest CO2 emissions of all. 
	- A second bar graph is placed at the bottom of the page, where we can see the various sectors, each divided by state and city.
If you click on the TX bar, you will notice only the cities in TX will be highlighted in the sector bar graph.

In the Excel Dashboard Blueprint, you will find the following:
- Description of the tools used for the final dashboard
- Description of the interactive element
- Analysis for the visualizations
- Future visualization ideas and recommendations for improving current visualization

## Link to the Presentation
[link to Google Slides Presentation](https://docs.google.com/presentation/d/e/2PACX-1vS_3j0Or_IGgdZwBIAsJDioPNrLeFdTmpARP94NagTTQFHqumSYEkyejG5D58UHU30W4D99TDhUWuLx/pub?start=false&loop=false&delayms=3000)

## Summary and Recommendations for the Dashboard
- We have opted for a blend of Plotly and Tableau in order to build an interactive website with informative data and accompanying visuals. 
- We also used various forms of filtering (by Year, Top 10 countries ect) to allow for a more comprehensive study of the charts provided.
- We used the Actions option in Tableau Dashboard, to include interactive selection and filtering elements to our visualization.
![actions](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Dashboard%20Images/Creating%20actions.png)

At first glance, we can see that TX is the largest CO2 emitter in the country, followed by LA. 
When we click on the TX bar in the bar graph, we can see how these emissions are spread out over the various sectors. Chemicals sector is the highest contributor.
![TX1](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Dashboard%20Images/Statewise_Emissions_TX.png)

We also notice the the Chemical sector is the highest contributing sector for CO2 emission in LA. 
![LA1](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Dashboard%20Images/Statewise_Emissions_LA.png)

As the first step to our analysis, we can assume that Texas and Louisiana are high on our priority list of states needing assistance in cutting down their CO2 emissions, especially in the Chemicals sector.
![TX2](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Dashboard%20Images/Analysis_state_sector_TX.png)
![LA2](https://github.com/sahithig1/capstone_greenhouse_emissions/blob/main/Dashboard%20Images/Analysis_state_sector_LA.png)

We may need to look into the companies that emit the highest amounts of CO2 and see if they would be a good match for this investment goal.


