'''
Created on Oct 21, 2017

@author: Tudor
'''
import sys
from sort_utility import sort_by_apartment, sort_by_type
from syntax import input_syntax
from copy import deepcopy


def exit(ops, apartments, Stack):
    #This method exits the program
    sys.exit(0)
    
def create_apartment(apartment_id, type, amount):
    #This method creates an apartment
    #input: apartment_id = the id of the apartment
    #       type = the type of expense for the apartment
    #       amount = the amount of the expense of a type for the apartment
    #output: apartment = a dictionary representing an apartment
    
    apartment = {"apartment_id": apartment_id, "type": type, "amount": amount}
    return apartment

def search(apart, apartments):
    #This function searches a specific apartment in the list of apartments
    #input: apart = the apartment that is searched
    #       apartments = the list of apartments
    #output: the position 'i' in the list of the searched apartment or -1 if it does not exit in the list
    
    for i in range(0, len(apartments)):
        if apartments[i]["apartment_id"] == apart[0] and apartments[i]["type"] == apart[1]:
            return i;
    return -1;

def sum(ops, apartments, Stack):
    #This method calculates the sum of expenses for a certain type for all the apartments
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #       apartments = the list with apartments 
    #output: expenses = the sum of expenses
    
    if len(ops) != 2:
        print("Invalid input! Read again the instructions!")
        return 
    
    type = ops[1]
    expenses = 0
    for apartment in apartments:
        if apartment["type"] == type:
            expenses += apartment["amount"]
    print("The total amount for the expenses having type", type, "is", expenses)
    return expenses

def max(ops, apartments, Stack):
    #This method prints the maximum amount per each expense type for an apartment
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #       apartments = the list with apartments 
    #output: maxx = the maximum
    
    if len(ops) != 2:
        print("Invalid input! Read again the instructions!")
        return 
    
    maxx = 0
    my_apartment = int(ops[1])
    type = ""
    for apartment in apartments:
        if apartment["apartment_id"] == my_apartment and apartment["amount"] > maxx:
            maxx = apartment["amount"]
            type = apartment["type"]
    print("The maximum amount per each expense type for apartment", my_apartment, "is", maxx, "for", type);
    return maxx
    
def sort(ops, apartments, Stack):
    #This method prints sorts either the apartments ascending by total amount of expenses, or writes the total amount of expenses for each type, 
    #sorted ascending by amount of money.
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #       apartments = the list with apartments 
    #output: -
    
    if len(ops) != 2:
        print("Invalid input! Read again the instructions!")
        return
    
    if ops[1] == "apartment":
        return sort_by_apartment(apartments)
    elif ops[1] == "type":
        return sort_by_type(apartments)
    else:
        print("Invalid input! Read again the instructions!")
        
    
def my_type_filter(apartments, type):
    #This method creates a new list which contains only the expenses having a certain type
    #input: apartments = the list of apartments
    #       type = the type of expense that is filtered
    #output: new_list = the list with  the expenses having the given type
    
    new_list = []
    for apartment in apartments:
        if apartment["type"] == type:
            new_list.append(apartment)
    return new_list

def my_value_filter(apartments, value):
    #This method creates a new list which contains only the expenses having the amount smaller than a given value
    #input: apartments = the list of apartments
    #       value = the limit of the amount of expenses
    #output: new_list = the list with  the expenses having the the amount smaller than the given value
    
    new_list = []
    val = int(value)
    for apartment in apartments:
        if (apartment["amount"] < val):
            new_list.append(apartment)
    return new_list
        
def filter(ops, apartments, Stack):
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #output: apartments = the list with apartments after the filter
    
    if len(ops) != 2:
        print("Invalid input! Read again the instructions!")
        return 
    Stack.append(deepcopy(apartments))
    new_list = []
    if ops[1][0].isalpha():
        new_list = my_type_filter(apartments, ops[1])
    else:
        new_list = my_value_filter(apartments, ops[1])
    apartments[:] = new_list[:]
        


def undo(ops, apartments, Stack):
    #This method performs an undo – the last operation that has modified program data will be reversed
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #output: apartments = the previous list with apartments
    
    if len(ops) != 1:
        print("Invalid input! Read again the instructions!")
        return
    if len(Stack) == 0:
        print("You cannot make an undo operation right now. The current list is the initial list!")
        return
    
    apartments.clear()
    prev_list = Stack[len(Stack) - 1]
    Stack.pop()
    for it in prev_list:
        apartments.append(it)
    return apartments
    
