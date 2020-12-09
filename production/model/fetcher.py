class Fetcher:
    def __init__(self):
        super().__init__()

    def connect_to_database(self, database_name):
        print("connecting to ", database_name)

    def execute_query(self, query):
        print("executing query")
