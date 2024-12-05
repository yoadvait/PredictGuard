import numpy as np
from src.data_processing.data_pipeline import DataProcessor

def test_data_processing():
    config = {}
    processor = DataProcessor(config)
    test_data = {'vibration': [1, 2, 3], 'temperature': [4, 5, 6]}
    
    # Test data processing
    processed_data = processor.process(test_data)
    assert processed_data.shape == (2, 3)