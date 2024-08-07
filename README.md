# House Price Prediction System
## Description
This web application predicts house prices based on user inputs. It uses three machine learning algorithms—Linear Regression, Random Forest Regressor, and Gradient Boosting Regressor—combined in a stacking model to provide accurate predictions. Users can input details such as average area income, house age, number of rooms, number of bedrooms, and population to get an estimated house price.
## Installation
### Prerequisites
- Python 3.11.5
- Flask
- Flask-SQLAlchemy
- NumPy
- Joblib
- Scikit-learn
- Pandas
### Installing
1. Clone the repository:
    ```sh
    git clone https://github.com/dilnadileep/house_price_prediction_application.git
    ```
2. Navigate to the project directory:
    ```sh
    cd project
    ```
3. Create virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Run the Flask application:
    ```sh
    flask run
  ## Usage
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Fill in the form with the required details (average area income, house age, number of rooms, number of bedrooms, population, and address).
3. Click the "Submit" button to get the predicted house price.
   <img width="960" alt="form submission" src="https://github.com/user-attachments/assets/cde4e7be-eee0-4e83-b7dd-3be5be5720ae">

5. The predicted price along with the house details will be displayed on the resulting page.
   <img width="960" alt="response" src="https://github.com/user-attachments/assets/1c8050cd-cb80-4750-9981-6021639c2051">

## Machine Learning Model
The core of this application is the machine learning model used for predicting house prices.
### Model Overview
- **Base Models**:
  - **Linear Regression**: A simple regression model that predicts the house price based on a linear relationship between features.
  - **Random Forest Regressor**: An ensemble method that uses multiple decision trees to improve prediction accuracy and robustness.
  - **Gradient Boosting Regressor**: A boosting technique that builds trees sequentially to correct errors made by previous models, enhancing prediction performance.

- **Stacking Model**:
  - The **Stacking Regressor** combines the predictions from the base models to form a meta-model (Linear Regression) that learns how to best combine the base models' predictions.
  - This ensemble approach leverages the strengths of each base model and reduces the overall prediction error.

### Model Training
1. **Dataset**: The model is trained on the `USA_Housing.csv` dataset, which includes features like average area income, house age, number of rooms, number of bedrooms, and population.  Dataset Downloaded from [https://www.kaggle.com/datasets/vedavyasv/usa-housing?resource=download]
2. **Feature Scaling**: The features are standardized using `StandardScaler` to ensure that all features contribute equally to the model's performance.
3. **Training**: The stacking model is trained on the scaled training data and evaluated on the test data.
4. **Performance Metrics**: The model's performance is assessed using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score.
   <img width="799" alt="image" src="https://github.com/user-attachments/assets/962cf42b-7a67-474b-a697-9c4ddbf7194b">


### Model Files
- **stacking_house_price_model.pkl**: The trained stacking model saved using Joblib.
- **scaler.pkl**: The scaler used to standardize the features before prediction.

## Model Training
1. Run the `train_model.py` script to train the model:
    ```sh
    python train_model.py
    ```
2. This script loads the dataset, preprocesses it, trains the stacking model, and saves the trained model and scaler to disk.

## Conclusion
This House Price Prediction System showcases the power of ensemble machine learning techniques to provide accurate and reliable predictions for house prices based on various input features. By combining the strengths of Linear Regression, Random Forest Regressor, and Gradient Boosting Regressor through a stacking approach, the model is able to leverage multiple algorithms to enhance prediction performance and handle complex relationships in the data.

## Contact
- **Name**: Dilna Dileep
- **Email**: dilnadileep002@gmail.com
- **GitHub**: (https://github.com/dilnadileep)

     
