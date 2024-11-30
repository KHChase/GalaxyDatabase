
import csv
from hash_table import HashTable

#converts csv to hash table(s) to only have to load once
def csv_to_hash(file_path, index_cols):
    hash_tables = {col: HashTable() for col in index_cols}

    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            for col in index_cols:
                # only insert if key is not None or empty
                key = row.get(col)
                if key:
                    hash_tables[col].insert(key, row)

    return hash_tables

# write any modifications done back to the csv file
def write_to_csv(file_path, hash_tables, index_cols):


    print(f"Changes successfully written to {file_path}")