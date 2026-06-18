# Car Price Prediction

## Project Overview
This project predicts the selling price of a used car using Machine Learning.

The model is trained using various car features such as:

- Present Price
- Driven Kilometers
- Number of Previous Owners
- Fuel Type
- Selling Type
- Transmission Type
- Car Age

## Dataset
The dataset contains information about used cars and their selling prices.

## Data Preprocessing
- Removed unnecessary columns
- Created Car_Age feature
- Applied One-Hot Encoding to categorical variables
- Split data into training and testing sets

## Model Used
Random Forest Regressor

## Model Performance
R² Score: **0.92**

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

## Files
- Dataset.csv
- car_price_model.pkl
- Task_3_Car_PricePrediction.ipynb

## Future Improvements
- Build Flask Web Application
- Deploy Model Online
- Improve UI/UX