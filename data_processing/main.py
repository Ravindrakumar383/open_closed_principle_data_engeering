from processors.json_data_processor import JSONDataProcessor
from processors.parquet_data_processor import ParquetDataProcessor
from processors.delta_data_processor import DeltaDataProcessor
from data_sources.json_data_source import JSONDataSource
from data_sources.parquet_data_source import ParquetDataSource
from data_sources.delta_data_source import DeltaDataSource
from pyspark.sql import SparkSession

def create_spark_session(app_name):
    return SparkSession.builder.appName(app_name).getOrCreate()

if __name__ == "__main__":
    
    spark = create_spark_session("DataProcessor")
    json_data_source = JSONDataSource("data.json", spark)
    parquet_data_source = ParquetDataSource("data.parquet", spark)
    delta_data_source = DeltaDataSource("delta_table", spark)
    

    json_processor = JSONDataProcessor(spark)
    parquet_processor = ParquetDataProcessor(spark)
    delta_processor = DeltaDataProcessor(spark)
    
    json_data = json_data_source.read()
    parquet_data = parquet_data_source.read()
    delta_data = delta_data_source.read()
   

    processed_json = json_processor.process_data(json_data)
    processed_parquet = parquet_processor.process_data(parquet_data)
    processed_delta = delta_processor.process_data(delta_data)
    

    spark.stop()