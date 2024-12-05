import yaml
from typing import Dict, Any

def load_config(config_path: str = 'config.yaml') -> Dict[str, Any]:
    """
    Load configuration from YAML file
    
    Args:
        config_path (str): Path to configuration file
    
    Returns:
        Dict: Loaded configuration dictionary
    """
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {
            'sensors': {
                'types': ['vibration', 'temperature'],
                'sampling_rate': 1000
            },
            'ml_models': {
                'anomaly_threshold': 0.85,
                'prediction_horizon': 30
            }
        }
    