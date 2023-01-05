# capstone_greenhouse_emissions
## Database
### Data Collection  
We used a python library(wbgapi) that fetches World Bank Data directly into the dataframe using API. 

### Data Cleaning and Analysis
Pandas is used to clean the data and perform an exploratory analysis.

### Database Storage
Postgres(SQL) is the database we intend to use, and the structure of the database is designed using the QuickDBD tool. We will eventually run the database in AWS.

The ERD diagram is shown below,
![](images/api_data_ERD.png?raw=true)

* Database stores static data for use during the project.
![](images/ghg_emissions_sample_data.png?raw=true)

* Database interfaces with the project in some format (database connects to the model)
![](images/MLconnected_db.png?raw=true)
