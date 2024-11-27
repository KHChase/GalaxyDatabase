import csv #needed to read in csv

#had to figure out which directory it's operating out of to know where to save Galaxy.csv
import os
print(os.getcwd())

#Hash Tables class to store keys and values
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        if key not in self.table:
            self.table[key] = []

        self.table[key].append(value)

    def search(self, key):
        return self.table.get(key, None)


#converts csv to hash table(s) to only have to load once

def csv_to_hash(file_path, index_cols):
    hash_tables = {col: HashTable() for col in index_cols}

    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            for col in index_cols:

                #only insert if key is not None or empty
                key = row.get(col)
                if key:
                    hash_tables[col].insert(key, row)

    return hash_tables


#main function

file_path = 'Galaxy.csv'

#columns to search by
index_cols = ['Galaxy', 'Seyfert_Type', 'PlateScale', 'pc_arcsecond', 'Redshift', 'Distance_Mpc', 'Xray_Lum14195kev', 'ColumnDensity_LognH', 'Obs_date', 'PSF']

hash_tables = csv_to_hash(file_path, index_cols)

search_galaxy = 'Circinus'
result = hash_tables['Galaxy'].search(search_galaxy)

if result:
    print(result)

else:
    print(f"No results found for '{search_galaxy}'")






