from pydantic import BaseModel
from typing import List

class DataModel(BaseModel):
    """Modelo de entrada para la API. Define las variables de entrada para la predicción."""
    
    u: float
    g: float
    r: float
    i: float
    z: float
    GALAXY: int
    QUASAR: int
    STAR: int

    def columns(self):
        """Retorna los nombres de las columnas en el orden correcto para el modelo."""
        return ["u", "g", "r", "i", "z", "GALAXY", "QUASAR", "STAR"]
    

class DataModelList(BaseModel):
    """Permite recibir múltiples registros en una sola petición."""
    
    data: List[DataModel]
