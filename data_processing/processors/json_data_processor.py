from processors.spark_data_processor import SparkDataProcessor

class JSONDataProcessor(SparkDataProcessor):
    def process_data(self, data):
        # Implement data processing logic for JSON data
        processed_data = data.select("column1", "column2").filter(data["column3"] > 10)
        return processed_data