'''
Created on Oct 30, 2017

@author: Tudor
'''
def calculate_expenses(my_apartment, apartments):
    #This method calculates the total expenses for an apartment
    #input: my_apartment = the apartment for which the method calculates the total amount of expenses
    #       apartments = the list of apartments
    #output: expenses = the total amount of expenses for the given apartment
    
    expenses = 0
    for apartment in apartments:
        if apartment["apartment_id"] == my_apartment:
            expenses += apartment["amount"]
    return expenses 

def calculate_expenses_by_type(my_type, apartments):
    #This method calculates the total expenses for a certain type
    #input: my_type = the type for which the method calculates the total amount of expenses
    #       apartments = the list of apartments
    #output: expenses = the total amount of expenses for the given type
    expenses = 0
    for apartment in apartments:
        if apartment["type"] == my_type:
            expenses += apartment["amount"]
    return expenses