SELECT * FROM country;
SELECT * FROM ghg_emissions;
SELECT * FROM sector_emissions;

select c.country_name, 
       e."year", 
	   e.sector_name,
	   e.emissions 
	   from sector_emissions as e 
	   join country as c 
	   on e.country_code = c.country_code;
	   
select c.country_name, 
       e.* from ghg_emissions as e 
	   join country as c 
	   on e.country_code = c.country_code;