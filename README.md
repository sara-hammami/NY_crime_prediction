# NY_crime_prediction

## Overview

A straightforward web application designed to estimate the likelihood of a crime occurring in New York City based on user-provided information, geographical location, and timestamp

## Dataset

This dataset includes all valid felony, misdemeanor, and violation crimes reported to the New York City Police Department (NYPD) from 2006 to the end of last year (2019). The dataset is publicly available and can be accessed [here](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i). It provides valuable insights into the various types of crimes reported in New York City over the years.

## Work Done

We have performed the following steps:

1. **Data Preprocessing**: Cleaned and preprocessed the raw dataset to handle missing values, standardize formats, and prepare it for model training.

2. **Model Training**: Utilized the XGBoost machine learning algorithm to train a predictive model. The model aims to predict the class of crime likely to happen based on various features such as time, location, age, gender, and race.

3. **Integration with Streamlit App**: Integrated the trained model into a Streamlit web application. This allows users to interactively input their information and receive predictions on the likelihood of being a victim of a particular crime.

4. **Map Integration with NYC Locate API**: Integrated the [NYC Locate API](https://locatenyc.io/) to access mapping functionality. Users can select their location on the map, and the application will use this information for crime predictions.

## Technologies
- Streamlit: A Python library for creating interactive web applications with minimal code.

- Folium: A Python library for creating interactive maps.


For data cleaning, exploratory data analysis (EDA), and modeling, we used the following Python libraries:

- Pandas: A powerful data manipulation and analysis library.

- seaborn: A statistical data visualization library based on Matplotlib.

- matplotlib: A comprehensive library for creating static, animated, and interactive visualizations in Python.

- Scikit-learn: A machine learning library for classical machine learning algorithms.

- LightGBM: A gradient boosting framework that uses tree-based learning algorithms.

- XGBoost: An optimized distributed gradient boosting library.

- CatBoost: A fast, scalable, and high-performance gradient boosting library.


## App Interface
![Web Application Screenshot](https://github.com/sara-hammami/NY_crime_prediction/blob/main/Capture.PNG)
## Contributors

- [Sarra Hammai ] (https://github.com/sara-hammami)
- [asma abidalli] (https://github.com/Asma-Ab)
- [mariem mezghani]
- [wissal oueslati] 

