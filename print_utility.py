'''
Created on Oct 21, 2017

@author: Tudor
'''
from total_expenses import calculate_expenses

def print_condition(cond, val, expenses):
    #This method validates a condition of printing for list_by_expenses method
    #input: cond = a code for the condition operator: 0 for '=', 1 for '>' and 2 for '<'
    #       val = the value to which we compare the total expenses for an apartment
    #       expenses = the total amount expenses for an apartment
    #output: True if the evaluated condition is true, otherwise False
    
    if cond == 0:
        if expenses == val:
            return True
        return False
    if cond == 1:
        if val < expenses:
            return True
        return False
    if val > expenses:
        return True
    return False


def list_all(apartments):
    #This method prints the entire list of apartments
    #input: apartments = the list of apartments
    #output: -
    if len(apartments) == 0:
        print("The list is empty!")
        return
    print("The entire list of current expenses is: ")
    for apartment in apartments:
        print(apartment["apartment_id"], apartment["type"], apartment["amount"])

def list_apartment(apart, apartments):
    #This method prints the expenses for a given apartment
    #input: apart = the apartment for which the method prints the expenses
    #       apartments = the list of apartments
    #output: -
    V = []
    for apartment in apartments:
        if apartment["apartment_id"] == apart:
            V.append(apartment)
    if len(V) == 0:
        print("There are no expenses for apartment ", apart, "!")
        return
    print("The current expenses for apartment ", apart, "are: ")
    for a in V:
        print(a["type"], a["amount"])
 

def list_by_expenses(ops, apartments):
    #This method prints all the apartments that have total amount of expenses '<', '=' or '>' than a given number
    #input: ops = a list that contains the tokens of the operation introduced by the user
    #       apartments  = the list of apartments
    #output: -
     
    calculated = [False] * 100005
    cond = 0
    if ops[1] == ">":
        cond = 1
    elif ops[1] == "<":
        cond = 2
    val = int(ops[2])
    print_some = False
    Ans = []
    for apartment in apartments:
        if calculated[apartment["apartment_id"]] == False:
            calculated[apartment["apartment_id"]] = True
            expenses = calculate_expenses(apartment["apartment_id"], apartments)
            if print_condition(cond, val, expenses) == True:
                print_some = True
                Ans.append(apartment["apartment_id"])
    if print_some == False:
        print("There are no apartments having total current expenses " + ops[1] + " " + ops[2] + "RON.")
    else:
        print("The apartments having total current expenses " + ops[1] + " " + ops[2] + "RON are: ")
        for i in Ans:
            print(i)