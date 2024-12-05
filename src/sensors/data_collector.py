import numpy as np
from typing import List, Dict, Any

class DataCollector:
    @staticmethod
    def preprocess_sensor_data(sensor_data: Dict[str, List[float]]) -> np.ndarray:
        """
        Preprocess and normalize sensor data
        
        Args:
            sensor_data (Dict): Raw sensor data
        
        Returns:
            np.ndarray: Preprocessed sensor data
        """
        # Convert to numpy array and normalize
        processed_data = np.array(list(sensor_data.values()))
        return (processed_data - processed_data.mean()) / processed_data.std()