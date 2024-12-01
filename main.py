
from csv_operations import csv_to_hash
from search import searchCase
from search import rangeSearch
from add_update import add_update


def main():
    file_path = 'Galaxy.csv'

    # converting csv to hash table
    hash_tables = csv_to_hash(file_path)

    # columns to be able to search by
    index_cols = []
    for col in hash_tables:
        index_cols.append(col)
    
    # while loop for initial user selection
    selection = 0
    while (selection != -1):
        print("\nWhat would you like to do? (Enter -1 to exit)")
        print("1. Perform a Search")
        print("2. Add/Update a Galaxy")
        print("3. Remove a galaxy")

        selection = int(input("\nEnter the number of your selection: "))

        while (selection != 1 and selection != 2 and selection != 3 and selection != -1):
            selection = int(input("Invalid selection. Please select from the list: "))

        # acts on user suggestion
        match selection:
            # searching
            case 1:
                print("\nEnter the number of the item you\'d like to search by:")
                print("1. Search by galaxy name")
                print("2. Search by header")
                choice = int(input("Search by: "))

                if choice == 1:
                    element = input("Enter the galaxy name to search for: ")
                elif choice == 2:
                    element = input("Enter the header name to search for: ")
                else:
                    print("Invalid choice. Returning to menu.")
                    continue

                searchCase(choice, element, hash_tables)

            # Adding/Updating
            case 2:
                add_update(hash_tables, index_cols, file_path)

            # Remove galaxy
            #case 3:


if __name__ == "__main__":
    main()
