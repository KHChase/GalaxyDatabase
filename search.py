
# Searching Function
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

#commenting out for time being   
# elif choice == 2:  # searching by header (column title)
        #if element in hash_tables:

           # print(f"\nData for header: {element}")
            #print("----------------------------------------------------")

            #for key, rows in hash_tables[element].table.items():
               # for row in rows:
                   # print(f"{element} for \"{row['Galaxy']}\": {row[element]}")
       # else:

 KHChase-search.py-rangeSearch
            print(f"\nHeader \'{element}\' not found in the hash tables.")

# searches data column for data within given range (inclusive)
# returns list of galaxies whose measurements fit range
# uses hash_tables version from my csv_operations.py update pull request
def rangeSearch(attribute, lower, upper, hash_tables):
    galaxies = []
    data = hash_tables[attribute].column()
    for i in data:
        num = float(i)
        if num >= lower and num <= upper:
            for j in hash_tables[attribute].search(i):
                galaxies.append(j)
    return galaxies
=======
            #print(f"\nHeader \'{element}\' not found in the hash tables.")
 main
