from processors.spark_data_processor import SparkDataProcessor

class ParquetDataProcessor(SparkDataProcessor):
    def process_data(self, data):
        # Implement data processing logic for Parquet data
        # Example: processed_data = data.select(...) or any transformation
        return processed_data
