# Earthquate data to be used for analysis.

Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

Fields: 
    date_time - combined date / time field
    date
    time
    latitude 
    longitude
    depth 
    mag - magnitude of the earthquake
    location - approximate location of the earthquake
    place - description of the epicenter where the earthquake occurred

    #####################################################

# Earthquake Data Analysis Project

This repository contains a data analysis project focused on earthquake events, using data sourced from the United States Geological Survey (USGS). The analysis aims to explore various aspects of global earthquake occurrences, including frequency, magnitude distribution, and geographic patterns.

## Project Overview

The project is designed to process and analyze a dataset of global earthquakes. The dataset includes information such as the date, time, location, magnitude, and depth of each earthquake. By performing a detailed analysis, the project answers key questions related to the characteristics of these seismic events.

### Key Objectives

- **Total Number of Earthquakes:** Determine the total number of recorded earthquakes within the dataset.
- **Magnitude Analysis:** Identify the number of earthquakes with a magnitude of 5 or greater, and calculate the average magnitude for earthquakes with depths greater than 100 km.
- **Geographic Distribution:** Analyze the geographic distribution of earthquakes to identify the location with the most recorded events.
- **Highest Magnitude:** Identify the earthquake with the highest magnitude in the dataset.

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:** pandas, numpy, matplotlib, seaborn
- **Data Source:** USGS Earthquake Catalog

## Getting Started

To run the analysis, clone this repository and ensure you have the required libraries installed. The data processing and analysis are contained in the `earthquake_analysis.ipynb` notebook.

```bash
git clone https://github.com/yourusername/earthquake-data-analysis.git
cd earthquake-data-analysis
pip install -r requirements.txt
```

## Data

The dataset used in this project is sourced from the USGS Earthquake Catalog. The data includes various attributes such as the event ID, timestamp, latitude, longitude, depth, and magnitude of each earthquake.

## Results

The results of the analysis provide insights into the distribution and characteristics of global earthquakes, highlighting regions with high seismic activity and the occurrence of significant seismic events.


