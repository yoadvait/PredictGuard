from typing import List, Dict

class MaintenanceRecordManager:
    def __init__(self):
        self.records: List[Dict] = []
    
    def add_record(self, record: Dict):
        """
        Add a maintenance record
        
        Args:
            record (Dict): Maintenance record details
        """
        self.records.append(record)
    
    def get_records(self) -> List[Dict]:
        """
        Retrieve all maintenance records
        
        Returns:
            List[Dict]: List of maintenance records
        """
        return self.records