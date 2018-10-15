'''
Created on Oct 24, 2017

@author: Tudor
'''

from total_expenses import calculate_expenses, calculate_expenses_by_type

def get_type(my_type, V):
    #This method searches the type of an expense in the list V
    #input: my_type = the type of expense that is searched
    #       V = the list of expenses
    #output: the position 'i' in the list of the searched expense type, or -1 is it doesn't exist
    
    for i in range(0, len(V)):
        if V[i][0] == my_type:
            return i
    return -1

def quicksort(left, right, V):
    #This is the well known quicksort algorithm, which sorts a list V in a Divide and Conquer method
    #input: left = the lower bound of the interval that we sort
    #       right = the upper bound of the interval that we sort
    #output: V = the sorted list
    
    i = left
    j = right
    mid = (i + j) >> 1
    pivot = V[mid][1]
    while i <= j:
        while V[i][1] < pivot:
            i = i + 1
        while V[j][1] > pivot:
            j = j - 1
        if i <= j:
            tmp = V[i]
            V[i] = V[j]
            V[j] = tmp
            i = i + 1
            j = j - 1
    if left < j:
        quicksort(left, j, V)
    if i < right:
        quicksort(i, right, V)
        
def sort_by_apartment(apartments):
    #This method writes the list of apartments sorted ascending by total amount of expenses.
    #input: apartment = the list of apartments
    #output V = the sorted list of apartments
    V = []
    calculated  = [False] * 10005
    for apartment in apartments:
        if calculated[apartment["apartment_id"]]:
            continue
        calculated[apartment["apartment_id"]] = True
        val = calculate_expenses(apartment["apartment_id"], apartments)
        V.append((apartment["apartment_id"], val))
    
    quicksort(0, len(V) - 1, V)
    print("The apartments sorted ascending by total amount of expenses: ")
    for i in V:
        print(i[0], "with", i[1], "RON")
    return V

    
def sort_by_type(apartments):
    #This method writes the total amount of expenses for each type, sorted ascending by amount of money.
    #input: apartment = the list of apartments
    #output V = the sorted list of apartments
    V = []
    for apartment in apartments:
        pos = get_type(apartment["type"], V)
        val = calculate_expenses_by_type(apartment["type"], apartments)
        if pos == -1: #if the current expense type doesn't exist in the list V
            V.append((apartment["type"], val))
    quicksort(0, len(V) - 1, V)
    print("The total amount of expenses for each type, sorted ascending by amount of money:")
    for i in V:
        print(i[0], "with", i[1], "RON") 
    return V       
            
    