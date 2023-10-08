from data_sources.data_source import DataSource

class JSONDataSource(DataSource):
    def __init__(self, source_path, spark_session):
        self.source_path = source_path
        self.spark_session = spark_session

    def read(self):
        json_data = self.spark_session.read.json(self.source_path)
        return json_data
