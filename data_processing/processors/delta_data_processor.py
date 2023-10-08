from processors.spark_data_processor import SparkDataProcessor

class DeltaDataProcessor(SparkDataProcessor):
    def process_data(self, data):
        # Implement data processing logic for Delta data
        # Example: processed_data = data.select(...) or any transformation
        return processed_data
