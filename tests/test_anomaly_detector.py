import numpy as np
from src.ml_models.anomaly_detector import AnomalyDetector

def test_anomaly_detection():
    config = {'anomaly_threshold': 0.85}
    detector = AnomalyDetector(config)
    test_data = np.random.rand(10, 5)
    
    # Test anomaly detection
    result = detector.predict(test_data)
    assert 'anomalies' in result
    assert 'scores' in result