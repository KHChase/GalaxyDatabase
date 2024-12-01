'''
    searches
        galSearch - return data for one galaxy
        colSearch - return data for one column
        
        rangeSearch - return all galaxies with values in range
        matchSearch - return all galaxies with values that match
        crossSearch - multiple of these
'''


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

# searches data column for data within given range (inclusive)
# returns list of galaxies whose measurements fit range
def rangeSearch(attribute, lower, upper, hash_tables):
    galaxies = []
    missed_galaxies = []
    missed = False
    data = hash_tables[attribute].column()
        
    for i in data:
        # check for range if possible
        try:
            num = float(i)
            if num >= lower and num <= upper:
                for j in hash_tables[attribute].search(i):
                    galaxies.append(j)
        # if check not possible, take note 
        except ValueError:
            missed = True
            for j in hash_tables[attribute].search(i):
                missed_galaxies.append(j)
            
    # let user know about missed_galaxies
    if missed:
        print("Not all galaxies were able to be checked for range.")
        print("Would you like to see uncheck galaxies?\n1. Yes\n2. No\n")
        choice = int(input("Enter selection: "))
        
        # FIXME: respond to choices
        # if you choose yes
        for g in missed_galaxies:
            print(g)
                
    return galaxies
