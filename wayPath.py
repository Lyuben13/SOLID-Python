from abc import ABC, abstractmethod

# Abstract base class for a data source
class DataSource(ABC):
    def __init__(self, path):
        self.path = path

    # Define interface for reading and writing data
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

# DataSource implementation for text files
class TextDataSource(DataSource):
    def read_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    def write_data(self, data):
        with open(self.path, 'w') as file:
            file.write(data)

# DataSource implementation for databases
class DbDataSource(DataSource):
    def read_data(self):
        return "data from database"

    def write_data(self, data):
        print(f"write {data} to database")

# Perform text operations using a DataSource
class TextOperations:
    def __init__(self, data_source):
        self.data_source = data_source
        self.data = self.data_source.read_data()

    # Returns True if the word is in the data
    def search_for_word(self, word):
        return word in self.data  # Fixed missing space

    # Returns the number of occurrences of a word in the data
    def count_occurrences(self, word):
        return self.data.count(word)

# Create DataSource instances
file = TextDataSource("..data.txt")
db = DbDataSource("customers")

# Use TextOperations with text file data source
obj = TextOperations(file)
print(f"Word 'more' found: {obj.search_for_word('more')}")
print(f"Occurrences of 'be': {obj.count_occurrences('be')}")

# Use TextOperations with database data source
obj = TextOperations(db)
print(f"Word 'data' found: {obj.search_for_word('data')}")
print(f"Occurrences of 'from': {obj.count_occurrences('from')}")
