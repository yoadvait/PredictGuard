import numpy as np
from typing import Dict, Any

class DataValidator:
    @staticmethod
    def validate(data: np.ndarray) -> bool:
        """
        Validate sensor data integrity
        
        Args:
            data (np.ndarray): Sensor data to validate
        
        Returns:
            bool: Validation result
        """
        # Check for NaN, infinite values, and data range
        return not (np.isnan(data).any() or 
                    np.isinf(data).any() or 
                    np.any(data < -1000) or 
                    np.any(data > 1000))
    