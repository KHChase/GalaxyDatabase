
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

            #print(f"\nHeader \'{element}\' not found in the hash tables.")
