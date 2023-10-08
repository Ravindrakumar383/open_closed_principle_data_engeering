from data_sources.data_source import DataSource

class DeltaDataSource(DataSource):
    def __init__(self, source_path, spark_session):
        self.source_path = source_path
        self.spark_session = spark_session

    def read(self):
        delta_data = self.spark_session.read.format("delta").load(self.source_path)
        return delta_data
