
import csv
from hash_table import HashTable
import os

#converts csv to hash table(s) to only have to load once
def csv_to_hash(file_path):
    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        index_cols = reader.fieldnames
        hash_tables = {col: HashTable() for col in index_cols}

        for row in reader:
            for col in index_cols:
                # only insert if key is not None or empty
                key = row.get(col)
                if key:
                    if col == index_cols[0]:
                        hash_tables[col].insert(key, row)
                    else:
                        hash_tables[col].insert(key, row.get(index_cols[0]))

    return hash_tables

# write any modifications done back to the csv file
def write_to_csv(galaxy_name, file_path, hash_tables):

    new_row = hash_tables["Galaxy"].search(galaxy_name)
    
    # Check if the file already exists
    file_exists = os.path.exists(file_path)
    
    # Write the data to the CSV file in append mode
    with open(file_path, mode='a', newline='') as file:
        if new_row:
            writer = csv.DictWriter(file, fieldnames=index_cols)
            
            # Write the header only if the file does not exist or is empty
            if not file_exists or os.stat(file_path).st_size == 0:
                writer.writeheader()
            
            writer.writerows(new_row)
            return True
        else:
            print("No data to append.")
            return False
