import numpy as np
from typing import Dict, Any

class DataProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    async def process(self, sensor_data: Dict) -> np.ndarray:
        """
        Process and prepare sensor data for analysis
        
        Args:
            sensor_data (Dict): Raw sensor data
        
        Returns:
            np.ndarray: Processed sensor data
        """
        processed_data = np.array(list(sensor_data.values()))
        return processed_data