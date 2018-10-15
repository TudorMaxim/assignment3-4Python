'''
Created on Oct 21, 2017

@author: Tudor
'''
from utility import create_apartment

#This module has only one method which introduces in the list the predefined list of 10 expenses

def predef_apartments(apartments):
    apartment = create_apartment(1, "gas",  10)  
    apartments.append(apartment)
    
    apartment = create_apartment(1, "water",  30)  
    apartments.append(apartment)
    
    apartment = create_apartment(1, "tv",  20)  
    apartments.append(apartment)
    
    apartment = create_apartment(2, "gas",  30)  
    apartments.append(apartment)
    
    apartment = create_apartment(2, "electricity",  10)  
    apartments.append(apartment)
    
    apartment = create_apartment(3, "gas",  10)  
    apartments.append(apartment)
    
    apartment = create_apartment(3, "water", 20)
    apartments.append(apartment)
    
    apartment = create_apartment(3, "internet",  80)  
    apartments.append(apartment)
    
    apartment = create_apartment(4, "gas",  50)
    apartments.append(apartment)
    
    apartment = create_apartment(4, "electricity",  20)  
    apartments.append(apartment)
   