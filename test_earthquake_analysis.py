# -*- coding: utf-8 -*-
"""
Unit tests for the functions defined in earthquake_analysis.
 
@author: Sackitey Joseph
"""

import earthquake_analysis, earthquake

def test_earthquake_count():
    
    # count of all earthquakes with magnitude above 0
    mag = 0
    
    #expected count of all earthquakes with magnitude above o
    expected_count = 97

    #actual returned count from the function
    
    computed_count = earthquake_analysis.earthquake_count(earthquake.data,mag)
    
    # variable to store if the test passed
    
    success = computed_count == expected_count
    
    # message to display if the test fails
    
    num_test_msg =f"computed {computed_count}, expected {expected_count}"
    
    
     # count of earthquakes with magnitudes above 5
     
    mag_above_five= 5
    
    #expected return from the function of all earthquakes with magnitudes above 5
    
    expected_output = 32

     # computed output from the function
     
    computed_output= earthquake_analysis.earthquake_count(earthquake.data,mag_above_five)
    
     # variable to store passed variables
     
    above_five_success= (computed_output==expected_output)
     # message to display if test fails
    
    above_five_test_msg=f"computed {computed_output}, expected {expected_output}"

    
    assert above_five_success, above_five_test_msg
    
    assert  success, num_test_msg
    
    
    

#test_number_of_earthquakes()

def test_max_location():
    
    #expected return from the function
    expected_output = [['Indonesia',13]]
    
    #actual returned string from the function
    
    computed_output = earthquake_analysis.max_location(earthquake.data)
    
    # variable to store if the test passed
    
    success = computed_output == expected_output
    
    # message to display if the test fails
    
    num_test_msg=f"computed {computed_output}, expected {expected_output}"
    
    assert  success, num_test_msg
    
    
#test_location_with_most_earthquake()    


def test_max_magnitude():    
  
    #expected return from the function
    expected_output = [['2023-10-23T10:10:15.384Z', '2023-10-23', '10:10:15', -29.9476, -177.5191, 23.092, 6, 'New Zealand', 'Kermadec Islands, New Zealand']]
    
    #actual returned string from the function
    
    computed_output = earthquake_analysis.max_magnitude(earthquake.data,)
    
    # variable to store if the test passed
    
    success = computed_output == expected_output
    
    # message to display if the test fails
    
    highest_test_msg=f"computed {computed_output}, expected {expected_output}"
    
        
    assert success, highest_test_msg
   
    
        
    
#test_highest_earthquake()


epsilon = 1e-10

def test_avg_magnitude():
    
    depth = 100
    
    #expected return from the function
    
    expected_output = 4.79
    
    #actual returned string from the function
    
    computed_output = float(f"{earthquake_analysis.avg_magnitude(earthquake.data,depth):.2f}")
    
    # variable to store if the test passed
        
    success = abs(expected_output - computed_output) < epsilon
    
    # message to display if the test fails
    
    num_test_msg=f"computed {computed_output}, expected {expected_output}"
    
    assert success,num_test_msg
    
    
if __name__ == "__main__":    
    test_avg_magnitude()  
    test_max_magnitude()
    test_max_location()
    test_earthquake_count()


