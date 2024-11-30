
from csv_operations import write_to_csv

def add_update(hash_tables, file_path):
    index_cols = []
    for col in hash_tables:
        index_cols.append(col)
    
    print("\nWould you like to add a new galaxy or update an existing one?")
    print("1. Add a new galaxy")
    print("2. Update an existing galaxy")
    choice = int(input("Choose an option (1 or 2): "))

    if choice == 1:
        new_data = {}
        for col in index_cols:
            new_data[col] = input(f"{col}: ").strip()

        galaxy_name = new_data['Galaxy']

        for col in index_cols:
            hash_tables[col].insert(new_data[col], new_data)

        write_to_csv(file_path, hash_tables, index_cols)
        print(f"\nGalaxy '{galaxy_name}' has been added successfully.")

    elif choice == 2:
        galaxy_name = input("\nEnter the name of the galaxy to update: ").strip()

        if galaxy_name not in hash_tables['Galaxy'].table:
            print(f"\nGalaxy '{galaxy_name}' not found.")
            return

        print(f"\nUpdating data for galaxy '{galaxy_name}'.")
        column_to_update = input(f"Enter the column name to update from {index_cols}: ").strip()

        if column_to_update not in index_cols:
            print(f"Invalid column name. Choose a column from {index_cols}")
            return

        new_value = input(f"Enter the new value for '{column_to_update}': ").strip()

        for col in index_cols:
            existing_data = [row for row in hash_tables[col].table.get(col, []) if row['Galaxy'] == galaxy_name]

            if existing_data:
                for row in existing_data:
                    row[column_to_update] = new_value

                hash_tables[col].insert(new_value, existing_data[0])

        write_to_csv(file_path, hash_tables, index_cols) # need to figure this out

        print(f"\nGalaxy '{galaxy_name}' has been updated in the '{column_to_update}' column.")
    else:
        print("Invalid choice.")
