from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.ai_models.air_quality_predictor import AirQualityPredictor
import numpy as np

class AirQualityPredictionView(APIView):
    predictor = AirQualityPredictor()

    def post(self, request):
        """
        Handle POST requests to predict air quality trends.
        """
        try:
            # Parse input data
            input_data = np.array(request.data.get("features", []))

            # Ensure the shape is correct
            if input_data.shape[1] != 5:
                return Response({"error": "Input data must have 5 features: ['pm2_5', 'pm10', 'no2', 'so2', 'o3']"}, status=status.HTTP_400_BAD_REQUEST)

            # Predict
            predictions = self.predictor.predict(input_data)

            return Response({"predictions": predictions.tolist()}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
