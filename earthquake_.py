# -*- coding: utf-8 -*-
"""
A program to analyze earthquake data in the past week.


@author: Sackitey Joseph

"""

import earthquake


def number_of_earthquakes(earthquake, magnitude=0):
    
    """
    Determines the number of earthquakes in the past week and 
    calculate the number of earthquakes with magnitude above or eqaul to a specified magnitude

    Parameters
    ----------
    earthquake : list
        A list of earthqaukes in the past week
        
    magnitude : int, optional
        It is the magnitude to determine the numbert of earthquakes with magnitude above it.
        The default is 0.

    Returns
    -------
    number_of_earthquake : int
    
        Value of the total number of earthquakes.
    above_magnitude : int
        Value of total number of earthquakes with magnitrude equal to or above specified magnitude.

    """
    
    number_of_earthquake = 0  
    above_magnitude = 0  
    number_of_earthquake = len(earthquake)
    
    if magnitude != 0:
        
        magnitudes_list = []

        for section in earthquake:
            magnitudes_list.append(section[6])

        for value in magnitudes_list:
            if value >= magnitude:
                above_magnitude += 1

    return number_of_earthquake, above_magnitude



def location_with_most_earthquake(earthquake):
    
    
    """
    Determines the location with most occurence of earthquakes

    Parameters
    ----------
    earthquake : list
        The list of all the data collected in the past week
 

    Returns
    -------
    common_name : string
        name of location with most occurence of earthquake

    """
    
    locations=[]
    common_name=[]
    for section in earthquake:
        locations.append(section[7])
    common_name.append(max(locations, key=locations.count))
    
    for name in common_name:
        print(name)
              
    return name




def highest_earthquake(earthquake):
    
    
    """
    Determines the name highest magnitude of earthquake and where it was recorded

    Parameters
    ----------
    earthquake : list
        The list of all the data collected in the past week.

    Returns
    -------
    name_of_place : string
        name of place with highest magnitude of earthquake
    highest_earthquake : int
        magnitude of the highest earthquake recorded

    """
    
    magnitudes_list=[]
    name_of_place=[]
    for section in earthquake:
        
        magnitudes_list.append(section[6])
    
    highest_earthquake = max(magnitudes_list)
    for section in earthquake:
        if section[6]== highest_earthquake:
            name_of_place.append(section[8])
    for name in name_of_place:
        print(name)        
    
    return name, highest_earthquake




def average_earthquake(earthquake,default_depth=100):
    
    
    """
    Calculates average magnitude of all earthquakes with depth grester than 100

    Parameters
    ----------
    earthquake : list
        The list of all the data collected in the past week.


    Returns
    -------
    average_magnitude : int
        average magnitude of earthquakes with depth above 100

    """
    
    depth_list=[]
    
    magnitudes_list=[]
    average_list=[]    

    for section in earthquake:
        
        magnitudes_list.append(section[6])
        
        depth_list.append(section[5])
        
    for depth in depth_list:
        if depth > default_depth:
            average_list.append(magnitudes_list[depth_list.index(depth)])
            
    average_magnitude= sum(average_list)/len(average_list)
    
    return average_magnitude






print("Earthquake Data for the Past Week")
print()
def main():
    
    """
    Prints out the returns of the various functions.

    Returns
    -------
    None.

    """
    
    magnitude= 5          # Magnitude to be compared can be varied here
    
    depth= 100           #depth to be used can be varied here
    
    
    number_earthquake, magnitude_above_five = number_of_earthquakes(earthquake.data,magnitude)
    location_name= location_with_most_earthquake(earthquake.data)
    name_of_place,highest_ =highest_earthquake(earthquake.data)
    average_mag=average_earthquake(earthquake.data,depth)
    print(f"Number of Earthquakes: {number_earthquake}\n\nEarthquake with magnitude of {magnitude} or above: {magnitude_above_five}\n")
    
    print(f"Location with most earthquakes: {location_name}\n")
    print(f"Magnitude of highest recorded earthquake: {highest_}\n")
    print(f"Highest earthquake recorded at: {name_of_place}\n")
    print(f"Average magnitude of earthquake with depth greater than {depth}: {average_mag:.2f}\n")
    
    
    
# calling the main function to print all outputs
main()    




