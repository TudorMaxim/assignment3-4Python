'''
Created on Oct 21, 2017

@author: Tudor
'''
import re
from print_utility import list_all, list_apartment, list_by_expenses
from utility import sum, max, filter, sort, undo, exit
from modify import add, remove, replace
from predefined_apartaments import predef_apartments
from syntax import input_syntax



##################### print function ##################### 

def list(ops, apartments, Stack):
    #This method prints the entire list of apartments, the expenses for a given apartment or
    #all the apartments that have total amount of expenses '<', '=' or '>' than a given number
    #input: ops = the list with tokens of the introduced operation
    #       apartments = the list of apartments
    #        Stack = the stack of previous lists of apartments
    #output: -
    
    if len(ops) == 1:
        list_all(apartments)
    elif len(ops) == 2:
        apart = int(ops[1])
        list_apartment(apart, apartments)
    elif len(ops) == 3:
        list_by_expenses(ops, apartments)
    else:
        print("Invalid input! Read again the instructions!")
        
        
##################### console function #####################
def run_console():
    #This is the console method, where the user introduces the input
    #input: an operation
    #output: -
    
    print(" Welcome to my application for Assignment03-04!")
    print(" This application helps an apartment building administrator to store, for a given month, the expenses for each apartment.")
    print(" Each expense is stored in the application using the following elements: apartment(number of apartment, positive integer),")
    print(" amount (positive integer), type (from one of the predefined categories: water, heating, electricity, gas, other).")
    input_syntax()
    operations = {"exit": exit, "add": add, "list": list, "replace": replace, "remove": remove, 
                  "sum": sum, "max": max, "sort": sort, "filter": filter, "undo": undo}
    apartments = []
    Stack = []
    predef_apartments(apartments)
    print("\nThe list already contains 10 items, which are: ")
    list_all(apartments)
    print("\nNow choose an operation from the list presented in the documentation or type 'exit' if you want to exit the program")
    
    while (True):
        print("Choose an operation")
        try:
            operation = input()
            ops = re.split(' ', operation)
            operations[ops[0]](ops, apartments, Stack)
        except KeyError:
            print("Invalid input! Read again the instructions!")
        except ValueError:
            print("Invalid input! Read again the instructions!")
        except IndexError:
            print("Invalid input! Read again the instructions!")
            
            