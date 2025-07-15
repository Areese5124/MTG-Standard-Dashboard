## MTG-Standard-Datalake
MTG Standard Datalake is a personal project I was working on to better learn Snowflake. The goals for this project is to create as series of dashboards and machline learning models which show current trends in the competitive scene of the Standard format in Magic the Gathering. To create these dashboards I needed to create a datalake which would store a variety of structured and semi structured data. This project was inspired by the [10th Edition Meta Data Dashboard](https://www.stat-check.com/the-meta) created by [Stat Check](https://www.facebook.com/StatCheck40k/) to track the meta in Warhammer 40k. 
# Overview of The Project
The data for the dashboard is pulled from two different places. All base card data id from [Scryfall](https://scryfall.com/) through the Scryfall API. All competitive data is from [MTG Goldfish](https://www.mtggoldfish.com/metagame/standard#paper), gathered using Selenium. The data is then cleaned and preprocessed. Copies of the data are then saved both locally and in Snowflake. Then through Snowflake Scripting, the tables and models then are updated automatically with the new data. 
# Project Timeline + Elements
- [x] Scryfall Api function
- [ ] MTG Goldfish scraper
- [X] Snowflake Data Pipe for insertion and loading
- [ ] Snowflake Dashboard Automation
- [ ] Snowflake ML Model Automation
