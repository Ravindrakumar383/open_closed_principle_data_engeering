from data_sources.data_source import DataSource


class ParquetDataSource(DataSource):
    def __init__(self, source_path, spark_session):
        self.source_path = source_path
        self.spark_session = spark_session

    def read(self):
        parquet_data = self.spark_session.read.parquet(self.source_path)
        return parquet_data
