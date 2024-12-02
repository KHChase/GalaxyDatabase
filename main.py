
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

    print("Which would you like to do: ")
    print("1. Perform a search")
    print("2. Add a galaxy")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        search.perform(hash_tables)
    
    elif choice == 2:
        add_update(hash_tables, index_cols, file_path)
    
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
