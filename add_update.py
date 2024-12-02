from csv_operations import write_to_csv

def add_update(hash_tables, index_cols, file_path):
    new_data = {}
    print("To enter a tab, enter ~")
    for col in index_cols:
        value = input(f"{col}: ").strip()
        new_data[col] = value.replace("~","\t")

    galaxy_name = new_data['Galaxy']

    for col in index_cols:
        hash_tables[col].insert(new_data[col], new_data)

    written = write_to_csv(galaxy_name, file_path, hash_tables, index_cols)
    
    if written:
        print(f"\nGalaxy '{galaxy_name}' has been added successfully.")
