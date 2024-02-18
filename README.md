# Automating Data Scrapers Apache Airflow
## Overview
This project focuses on scraping house rental data from the website "www.buyrentkenya.com". The goal is to extract various attributes such as titles, locations, number of bedrooms, number of bathrooms, descriptions, and prices of available rental properties. The project includes both a web scraping script and an automated workflow using Apache Airflow.

## Project Structure
* `main.py`: This Python script contains the code for scraping the rental data from the website.
* `buyrentkenya.py`: This python script contains the code for airflow automation and stores the data in a database.
* `buy_rent_kenya.csv`: The CSV file where the scraped data from the main.py is stored.
* `buyrentkenya.db`: SQLite database file where the scraped data is stored by the Apache Airflow DAG.
* `README.md`: This file provides an overview of the project, its objectives, and how to execute the script.

## Execution
To run the web scraping script:

- Ensure that you have Python installed on your system.
- Install the required libraries by running pip install pandas requests beautifulsoup4.
- Execute the script main.py.
- As for the airflow automation script, 

## Web Scraping Script Description
- The script sends a request to the specified URL using the requests library.
- It parses the HTML content of the response using BeautifulSoup.
- The script extracts relevant information such as titles, locations, number of bedrooms, number of bathrooms, descriptions, and prices of rental properties.
- Data from multiple pages is collected by iterating through page numbers.
- The scraped data is stored in a Pandas DataFrame and then saved to a CSV file named buy_rent_kenya.csv.

## Apache Airflow DAG Description
- The Apache Airflow DAG automates the execution of the web scraping script at specified intervals.
- The DAG is scheduled to run daily at 12:05 PM.
- It starts by creating a SQLite table if it does not exist already.
- The web scraping task collects rental data from the website and stores it in the SQLite database.
- The DAG utilizes task dependencies to ensure that tasks are executed sequentially.

# Dependencies
* Python 3.x
* Pandas
* Requests
* BeautifulSoup4
* Apache Airflow

## Execution
To run the web scraping script:

- Ensure that you have Python installed on your system.
- Install the required libraries by running pip install pandas requests beautifulsoup4.
- Execute the script web_scraping_script.py.
- To run the Apache Airflow DAG:

- Install Apache Airflow and initialize the Airflow database.
- Place the Buy_Rent_Kenya_Dag.py file in the Airflow DAGs folder.
- Start the Airflow scheduler and webserver.
- The DAG will automatically execute according to the specified schedule.

### Collaborators
1. [Brian Chacha](https://github.com/MarwaBrian)
2. [Mutai Gilbert](https://github.com/Mutai-Gilbert)
3. [Allan Silver](https://github.com/Adrian-Silver)

## Acknowledgments
Special thanks to Data Science East Africa, ALX_Kenya and Lux Academy for organizing the Data Science Hackathon.
