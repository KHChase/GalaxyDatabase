import csv #needed to read in csv

#Hash Tables class to store keys and values
class HashTable:
    def __init__(self):
        self.table = {}

    #insert into hash table
    def insert(self, key, value):
        if key not in self.table:
            self.table[key] = []

        self.table[key].append(value)

    #searching hash table
    def search(self, key):
        return self.table.get(key, None)


#converts csv to hash table(s) to only have to load once
def csv_to_hash(file_path):
    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        index_cols = reader.fieldnames
        hash_tables = {col: HashTable() for col in index_cols}

        for row in reader:
            for col in index_cols:

                #only insert if key is not None or empty
                key = row.get(col)
                if key:
                    hash_tables[col].insert(key, row)

    return hash_tables


#Searching Function
def searchCase(choice, element, hash_tables):

    if choice == 1:

        #search_galaxy = 'Circinus'
        result = hash_tables['Galaxy'].search(element)

        #if found, print entire results
        if result:
            for row in result:
                print("\n********************************************************")
                for header in row:
                    print(header, ": ", row[header])
                print("\n********************************************************")


    #if not found, prints message
        else:
            print(f"\nNO RESULTS FOUND FOR: \'{element}\'")
            print("----------------------------------------------------")



def main():

    file_path = 'Galaxy.csv'

    #converting csv to hash table
    hash_tables = csv_to_hash(file_path)



    #while loop for initial user selection

    selection = 0
    while (selection != -1):

        print("\nWhat would you like to do? (Enter -1 to exit)")
        print("1. Perform a Search")
        print("2. Add/Update a Galaxy")
        print("3. Remove a galaxy")

        selection = int(input("\nEnter the number of your selection: "))

        while (selection != 1 and selection != 2 and selection != 3 and selection != -1):
            selection = int(input("Invalid selection. Please select from the list: "))

        #acts on user suggestion
        match selection:

            #searching
            case 1:
                print("\nEnter the number of the item you\'d like to search by:")
                print("1. Search by galaxy name")
                print("2. Search by Seyfert Type")
                choice = int(input("Search by: "))

                element = input("Enter the galaxy name, distance, Seyfert Type, etc. to search for: ")

                #element = "Circinus"

                searchCase(choice, element, hash_tables)

            #Adding/Updating
            # case 2:
            #     print("Need to finish")
            #
            # #remove galaxy
            # case 3:
            #     #remove galaxy
            #     print("Need to finish")



if __name__ == "__main__": main()




