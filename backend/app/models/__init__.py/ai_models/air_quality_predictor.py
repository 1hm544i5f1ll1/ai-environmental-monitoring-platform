import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class AirQualityPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, data: pd.DataFrame):
        """
        Train the model using historical air quality data.
        :param data: DataFrame containing columns ['pm2_5', 'pm10', 'no2', 'so2', 'o3', 'target']
        """
        features = data[['pm2_5', 'pm10', 'no2', 'so2', 'o3']]
        target = data['target']

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)

        mse = mean_squared_error(y_test, predictions)
        print(f"Model trained. Mean Squared Error: {mse}")

    def predict(self, input_data: np.array):
        """
        Predict air quality trend based on input data.
        :param input_data: Numpy array with shape (n_samples, 5) for ['pm2_5', 'pm10', 'no2', 'so2', 'o3']
        :return: Predicted values
        """
        return self.model.predict(input_data)
