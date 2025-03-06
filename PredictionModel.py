import joblib
import pandas as pd

class Model:
    def __init__(self):
        """Carga el modelo y el pipeline de preprocesamiento al inicializar la clase."""
        self.pipeline = joblib.load("preprocessing_pipeline.joblib")
        self.model = joblib.load("linear_regression_model.joblib")

    def make_predictions(self, data):
        """
        Realiza predicciones con el modelo.
        
        Parámetros:
        - data (pd.DataFrame): Datos preprocesados para la predicción.

        Retorna:
        - Lista con las predicciones.
        """
        processed_data = self.pipeline.transform(data)  # Preprocesar los datos
        predictions = self.model.predict(processed_data)  # Realizar predicción
        return predictions.tolist()  # Convertir a lista JSON serializable


prediction_model = Model()
