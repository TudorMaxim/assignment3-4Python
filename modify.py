'''
Created on Oct 21, 2017

@author: Tudor
'''
from utility import search, create_apartment
from copy import deepcopy

def add_apartment(i, j, k, ops, apartments):
    #This method adds an apartment in the list of apartments
    #input: ops = the list with tokens of the introduced operation
    #       i, j, k = consecutive positions in ops. 'i' is for the apartment_id, 'j' is for the type and 'k' is for the amount
    #output: apartments = the list with apartments with the new expenses that are added
    
    apartment_id = int(ops[i])
    type = ops[j]
    amount = int(ops[k])
    apart = (apartment_id, type);
    pos = search(apart, apartments)
    if pos == -1:
        apartment = create_apartment(apartment_id, type, amount)
        apartments.append(apartment)
    else:
        apartments[pos]["amount"] += amount
        
def add(ops, apartments, Stack):
    #This method adds multiple new expenses in the list of apartments
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #output: apartments = the list with apartments with the new expenses that are added

    last = len(ops) - 1
    if ops[last][len(ops[last]) - 1] > '9' or  ops[last][len(ops[last]) - 1] < '0':
        print("Invalid syntax! The add operation cannot end with ','. Read again the instructions")
        return 
    
    Stack.append(deepcopy(apartments))
    for i in range(1, len(ops)):
        lg = len(ops[i]) - 1
        if (ops[i][lg] == ","):
            ops[i] = ops[i][:lg]
            add_apartment(i - 2, i - 1, i, ops, apartments)
    add_apartment(len(ops) - 3, len(ops) - 2, len(ops) - 1, ops, apartments)
    
    
def remove_by_apartment(first, last, apartments):
    #This method removes an interval [first, last] of apartments from the list of apartments
    #input: first = the lower bound of the interval
    #       last = the upper bound of the interval 
    #output: apartments = the new list of apartments
    
    i = 0
    while i < len(apartments):
        if apartments[i]["apartment_id"] >= first and apartments[i]["apartment_id"] <= last:
            apartments.pop(i)
        else:
            i = i + 1
    return apartments    

def remove_by_type(type, apartments):
    #This method removes all the expenses for a certain type from all apartments
    #input: type = the type of expenses that will be removed
    #output: apartments = the new list of apartments
    
    i = 0
    while i < len(apartments):
        if apartments[i]["type"] == type:
            apartments.pop(i)
        else:
            i = i + 1 
    return apartments
  
def remove(ops, apartments, Stack):
    #This method removes multiple new expenses from the list of apartments if the user wants to remove by the apartment_id, 
    #or removes the expenses for a certain type for all the apartments
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #output: apartments = the list with apartments without the expenses that are removed
    
    if len(ops) == 2 and ops[1].isalpha():
        Stack.append(deepcopy(apartments))
        type = ops[1]
        remove_by_type(type, apartments)
    elif len(ops) == 4 and ops[2] == "to":
        Stack.append(deepcopy(apartments))
        first = int(ops[1])
        last = int(ops[3])
        remove_by_apartment(first, last, apartments)
    else:
        last = len(ops) - 1
        if ops[last][len(ops[last]) - 1] > '9' or  ops[last][len(ops[last]) - 1] < '0':
            print("Invalid syntax! The remove operation cannot end with ','. Read again the instructions")
            return
        Stack.append(deepcopy(apartments))
        for i in range(1, len(ops) - 1):
            lg = len(ops[i]) - 1
            ops[i] = ops[i][ : lg]
            index = int(ops[i])
            remove_by_apartment(index, index, apartments)
        index = int(ops[len(ops) - 1])
        remove_by_apartment(index, index, apartments)
    
    return apartments    
    
            
def replace(ops, apartments, Stack):
    #This method replaces the amount for a type of expense for a given apartment
    #input: ops = the list with tokens of the introduced operation
    #       Stack = the stack of previous lists of apartments
    #output: apartments = the list with apartments with the replaced amounts
    
    Stack.append(deepcopy(apartments))
    apartment_id = int(ops[1])
    type = ops[2]
    new_amount = int(ops[4])
    apart = (apartment_id, type)
    pos = search(apart, apartments)
    if pos != - 1:
        apartments[pos]["amount"] = new_amount
    return apartments
        
        
        
        
        
        
        
        
        
        
        