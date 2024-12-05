from src.sensors.sensor_manager import SensorNetworkManager
import pytest

@pytest.mark.asyncio
async def test_sensor_data_collection():
    config = {'types': ['vibration', 'temperature'], 'sampling_rate': 1000}
    sensor_manager = SensorNetworkManager(config)
    
    # Test data collection
    sensor_data = await sensor_manager.collect_multimodal_data()
    assert len(sensor_data) == 2