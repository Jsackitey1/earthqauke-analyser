# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:31:38 2023

How many there were, how many with a magnitude of 5 or greater, 
which location had the most earthquakes, 
what earthquake(s) had the highest magnitude and where it took place, 
and the average magnitude of earthquakes with a depth greater than 100.

@author: Jonathan Hoffman
"""

import earthquake

def earthquake_count(data, min_mag = 0):
    """
    The count of all earthquakes with a magnitude greather than the min magnitude.
    By default, this will return the count of all earthquakes.

    Parameters
    ----------
    data : list
        The list of earthquakes to evaluate.
    min_mag : float, optional
        The minimum magnitude to include in the count. The default is 0.

    Returns
    -------
    count : int
        The count of earthquakes greater than the min magnitude.

    """
    
    #ALTERNATIVE
    #count = 0
    #for e in data:
    #    if e[6] >= min_mag:
    #        count += 1
            
    count = sum(1 for e in data if e[6] >= min_mag)
    
    return count


def max_location(data):
    """
    Finds the locations that had the most earthquakes

    Parameters
    ----------
    data : list
        The list of earthquakes to evaluate.

    Returns
    -------
    max_locations : list
        A list of the locations with the most earthquakes and the count.

    """
    
    #create a list for the locations with the most earthquakes
    max_locations = []
    #create list to store all locations with an earthquake
    all_locations = [l[7] for l in data]
    
    #get a list of the unique locations
    unique_locations = set(all_locations)
    
    #loop through the unique locations and determine the count of each
    #if the count is greater than the max count, reset the max list with the current location
    #if the count is equal to the max count, add that location to the list
    max_count = 0
    for location in unique_locations:
        count = all_locations.count(location)
        if count > max_count:
            max_locations = [[location, count]]
            max_count = count
        elif count == max_count:
            max_locations.append([location, count])

    return max_locations


def max_magnitude(data):
    """
    Finds all earthquakes with the highest magnitude.    

    Parameters
    ----------
    data : list
        The list of earthquakes to evaluate.

    Returns
    -------
    max_earthquake : list
        A list of the earthquakes with the higest magnitude.

    """

    #sort the data in reverse order by the magnitude
    sorted_data = sorted(data, key=lambda e: e[6], reverse=True)
       
    
    #find the max magnitured based on the first row in the sorted list
    max_mag = sorted_data[0][6]

    #loop through the list to find all magnitudes that match the max magnitude 
    max_earthquake = [e for e in sorted_data if e[6] == max_mag]
        
    #ALTERNATIVE
    # this may be faster over an extremely large data set since it stops
    # max_earthquake  = []
    # for e in sorted_data:
    #     mag = e[6]
    #     if mag == max_mag:
    #         max_earthquake.append(e)
    #     else:
    #         break

    #print(max_earthquake)
    return max_earthquake

def avg_magnitude(data, depth = 0):
    """
    Determine the average magnitued of all earthquakes with a depth greater than the value entered.
    By default, this will return the average of all earthquakes in the dataset. 

    Parameters
    ----------
    data : list
        The list of earthquakes to evaluate.
    depth : float, optional
        depth of the earthquakes to include in the average magnitude. The default is 0.

    Returns
    -------
    avg : float
        The average magnitude of the earthquakes with a depth greater than the input depth.

    """
    
    mag = [e[6] for e in data if e[5] > depth]
    avg = sum(mag) / len(mag)
    
    return avg

#Main Program Logic
if __name__ == "__main__":
    #Call each function and print out the results
    print("Total number of earthquakes: ", earthquake_count(earthquake.data))
    print()
    
    mag = 5
    print(f"Earthquakes with a magnitude of {mag} or higher: ", earthquake_count(earthquake.data, mag))
    print()
    
    #Loop through the locations with the most earthquakes
    locations = max_location(earthquake.data)
    print(f"There were {locations[0][1]} earthquakes in the location with the most earthquakes.\nThis occurred in: ")
    for e in max_location(earthquake.data):
        print(f"\t{e[0]}")
    print()
    
    #Loop through the earthquakes with the highest     
    place = max_magnitude(earthquake.data)
    print(f"The largest earthquake had a mangitude of {place[0][6]}.\nThis took place in: ")
    for e in max_magnitude(earthquake.data):
        print(f"\t{e[8]}")
    print()
    
    depth = 100
    print(f"The avgerage magnitude of all earthquakes with a depth greater than {depth}: {avg_magnitude(earthquake.data, depth):.2f}")
