
from csv_operations import csv_to_hash
import search
from add_update import add_update


def main():
    file_path = 'Galaxy.csv'

    # converting csv to hash table
    hash_tables = csv_to_hash(file_path)

    # columns to be able to search by
    index_cols = []
    for col in hash_tables:
        index_cols.append(col)

    search.perform(hash_tables)

if __name__ == "__main__":
    main()
