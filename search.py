
# Searching Function
def searchCase(choice, element, hash_tables):

    if choice == 1:
        # search_galaxy = 'Circinus'
        result = hash_tables['Galaxy'].search(element)

        # if found, print entire results
        if result:
            for row in result:
                print("\n********************************************************")
                print("Galaxy: ", row['Galaxy'])
                print("Seyfert Type: ", row['Seyfert_Type'])
                print("Plate Scale: ", row['PlateScale'])
                print("pc/\": ", row['pc_arcsecond'], )
                print("Redshift: ", row['Redshift'])
                print("Distance: ", row['Distance_Mpc'])
                print("X-ray: ", row['Xray_Lum14195kev'])
                print("Column-Density: ", row['Column_Density_LognH'])
                print("Obs_date: ", row['Obs_date'])
                print("PSF: ", row['PSF'])
                print("\nCentral 200 pc Log[Luminosity]")
                print("------------------------------------")
                print("H2 (erg/s): ", row['H2 (erg/s)(Central 200 pc Log[Luminosity])'])
                print("[Si VI (erg/s): ", row['[Si VI] (erg/s)(Central 200 pc Log[Luminosity])'])
                print("Br-Ga (erg/s): ", row['Br-Ga (erg/s)(Central 200 pc Log[Luminosity])'])

                print("\nHWHM")
                print("------------------------------------")
                print("H2(pc): ", row['H2 (pc) (HWHM)'])
                print("[Si VI](pc): ", row['[Si VI] (pc)(HWHM)'])
                print("Br-Ga(pc): ", row['Br-Ga (pc)(HWHM)'])

                print("\n********************************************************")
        else:
            print(f"\nNO RESULTS FOUND FOR: \'{element}\'")
            print("----------------------------------------------------")

    elif choice == 2:  # searching by header (column title)
        if element in hash_tables:

            print(f"\nData for header: {element}")
            print("----------------------------------------------------")

            for key, rows in hash_tables[element].table.items():
                for row in rows:
                    print(f"{element} for \"{row['Galaxy']}\": {row[element]}")
        else:

            print(f"\nHeader \'{element}\' not found in the hash tables.")