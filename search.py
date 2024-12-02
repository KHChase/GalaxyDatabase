'''
    searches
        galSearch - return data for one galaxy
        colSearch - return data for one column
        valSearch - return a specific value for a specific galaxy
        
        rangeSearch - return all galaxies with values in range
        matchSearch - return all galaxies with values that match
        crossSearch - multiple of these
'''

# walks user through searching
def perform(hash_tables):
    # FIXME: prompt user to input their preferred search
    print("What would you like to search by? (Enter 1-4, or -1 to exit)")
    print("1. Search by galaxy")
    print("2. Search by column")
    print("3. Search for a galaxy's specific value")
    print("4. Search by multiple values")
    choice = int(input("\nSearch by: "))
    
    match choice:
        case 1:
            g = input("\nEnter the galaxy name: ")
            results = galSearch(g, hash_tables)
        case 2:
            a = input("\nEnter the column Title: ")
            results = colSearch(a, hash_tables)
        case 3:
            g = input("Enter the galaxy name: ")
            a = input("Enter the column title: ")
            results = valSearch(g, a, hash_tables)
            print(f"\n{a} for {g}: {results}")
        case 4:
            results = crossSearch(hash_tables)
            choice2 = int(input("Print galaxies found? 1. Yes, 2. No: "))
            if choice2 == 1:
                for r in results:
                    galSearch(r, hash_tables)
    return results
    


# prints and returns all data for one galaxy
def galSearch(galaxy, hash_tables):
    try:
        result = hash_tables['Galaxy'].search(galaxy)
        for row in result:
            print("\n********************************************************")
            for header in row:
                print(header, ": ", row[header])
            print("\n********************************************************")
        return result
    except TypeError:
        print("ERROR: Galaxy ", galaxy, " is not in database.")
        return


# returns all data from one column
# not the same as returning the column, this is a List and not part of a HashTable
def colSearch(attribute, hash_tables):
    try:
        result = hash_tables[attribute].column()
    except KeyError:
        print("ERROR: ", attribute, "not in database.")
        return []

    vals = []
    for i in result:
        rows = hash_tables[attribute].search(i)
        if rows:
            vals.append(i)
    return vals
    

# return a specific value for a specific galaxy
def valSearch(galaxy, attribute, hash_tables):
    try:
        result = hash_tables['Galaxy'].search(galaxy)
    except TypeError:
        print("ERROR: Galaxy", galaxy, "is not in database.")
        return
    val = result[0].get(attribute)
    
    if val == None:
        print("ERROR:", attribute, "is not in database.")
    return val


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
        choice = int(input("Enter 1 or 2: "))
        
        if choice == 1:
            for g in missed_galaxies:
                print(g)
                
    return galaxies
    
    
# searches data column for data within given value
# returns list of galaxies that has value
def matchSearch(attribute, target, hash_tables):
    galaxies = []
    try:
        data = hash_tables[attribute].column()
    except KeyError:
        print("ERROR: ", attribute, "not in database.")

    for i in data:
        # since this is checking strings it should
        if i == target:
            for j in hash_tables[attribute].search(i):
                galaxies.append(j)

    return galaxies


# returns list of galaxies that fit multiple matchSearch / rangeSearch
# user refines search in steps
def crossSearch(hash_tables):
    galaxies = colSearch("Galaxy", hash_tables)
    exit = False
    while not exit:
        choice = int(input("range (1), match (2), or exit (-1): "))
        # perform limiting search
        match choice:
            case 1:
                attribute = input("attribute: ")
                lower = float(input("lower bound: "))
                upper = float(input("upper bound: "))
                limit = rangeSearch(attribute, lower, upper, hash_tables)
            case 2:
                attribute = input("attribute: ")
                target = input("target: ")
                limit = matchSearch(attribute, target, hash_tables)
            case -1:
                exit = True
                
        # update limit_tables to reflect search
        save = []
        for i in limit:
            if galaxies.count(i) > 0:
                save.append(i)
        galaxies = save
        print("Search currently returns: ", len(galaxies), "\n")
    return galaxies
