'''
Created on Oct 23, 2017

@author: Tudor
'''
from utility import *
from sort_utility import *
from modify import *
from total_expenses import *
from predefined_apartaments import predef_apartments
from copy import deepcopy

############### utility test functions ###############
def test_create_apartment():
    a = {"apartment_id": 1, "type": "water", "amount": 10}
    b = create_apartment(1, "water", 10)
    assert a == b
    
def test_search():
    V = []
    predef_apartments(V)
    apart = (1, "water")
    assert search(apart, V) == 1
    
def test_sum():
    V = []
    Stack = []
    predef_apartments(V)
    ops = ["sum", "gas"]
    assert sum(ops, V, Stack) == 100

def test_max():
    V = []
    Stack = []
    predef_apartments(V)
    ops = ["max", "1"]
    assert max(ops, V, Stack) == 30 

def test_sort_by_apartment():
    V = []
    V.append(create_apartment(1, "gas", 30))
    V.append(create_apartment(1, "water", 50))
    V.append(create_apartment(2, "tv", 20))
    V.append(create_apartment(3, "electricity", 10))
    V.append(create_apartment(4, "gas", 50))
    A = [(3, 10), (2, 20), (4, 50), (1, 80)]
    assert sort_by_apartment(V) == A

def test_sort_by_type():
    V = []
    V.append(create_apartment(1, "gas", 30))
    V.append(create_apartment(1, "water", 50))
    V.append(create_apartment(2, "tv", 20))
    V.append(create_apartment(3, "electricity", 10))
    V.append(create_apartment(4, "gas", 50))
    A = [("electricity", 10), ("tv", 20), ("water", 50), ("gas", 80)]
    assert sort_by_type(V) == A

def test_quicksort():
    V = [(1, 2), (2, 1), (3, 5), (4, 4), (5, 3)]
    A = [(2, 1), (1, 2), (5, 3), (4, 4), (3, 5)]
    quicksort(0, 4, V)
    assert V == A

def test_get_type():
    V = [("gas", 1), ("water", 2), ("tv", 3)]   
    my_type = "water"
    assert get_type(my_type, V) == 1
     
def test_sort():
    test_get_type()
    test_quicksort()
    test_sort_by_apartment()
    test_sort_by_type()

def test_my_value_filter():
    V  = []
    predef_apartments(V)
    val = 15
    A = [create_apartment(1, "gas",  10), create_apartment(2, "electricity",  10), create_apartment(3, "gas",  10), create_apartment(4, "electricity",  10)]
    assert my_value_filter(V, val) == A

def test_my_type_filter():
    V = []
    type = "gas"
    predef_apartments(V)
    A = [create_apartment(1, "gas",  10), create_apartment(2, "gas",  30), create_apartment(3, "gas",  10), create_apartment(4, "gas",  50)]
    assert my_type_filter(V, type) == A
    

def test_filter():
    test_my_type_filter()
    test_my_value_filter()
    
def test_undo():
    A = [create_apartment(1, "water", 20), create_apartment(2, "gas", 30)]
    B = [create_apartment(1, "water", 20), create_apartment(2, "gas", 30), create_apartment(3, "tv", 40)]
    ops = ["undo"]
    Stack = []
    Stack.append(deepcopy(A)) 
    assert undo(ops, B, Stack) == A
        
############# modify test functions ##################
def test_add():
    V = []
    W = []
    Stack = []
    ops = ["add", "1", "gas", "50"]
    apart = create_apartment(1, "gas", 50)
    W.append(apart)
    add(ops, V, Stack)
    assert V == W      
     
def test_replace():   
    V = []
    Stack = []
    predef_apartments(V)
    A = V
    A[0]["amount"] = 50
    ops = ["replace", "1", "gas", "with", "50"]
    assert replace(ops, V, Stack) == A

def test_remove_by_apartment():
    V = [create_apartment(1, "gas", 10), create_apartment(2, "gas", 10), create_apartment(1, "water", 10)]
    A = [create_apartment(2, "gas", 10)]
    assert remove_by_apartment(1, 1, V) == A

def test_remove_by_type():
    V = [create_apartment(1, "gas", 10), create_apartment(2, "gas", 10), create_apartment(1, "water", 10)]
    A = [create_apartment(1, "water", 10)]
    assert remove_by_type("gas", V) == A
    
def test_remove():
    test_remove_by_apartment()
    test_remove_by_type()
    Stack = []
    V = [create_apartment(1, "gas", 10), create_apartment(2, "gas", 10), create_apartment(3, "water", 10)]
    A = [create_apartment(2, "gas", 10)]
    ops = ["remove", "1,", "3"]
    assert remove(ops, V, Stack) == A

########### expenses calculation test functions ###############

def test_calculate_expenses():
    V = []
    predef_apartments(V)
    assert calculate_expenses(3, V) == 110

def test_calculate_expenses_by_type():
    V = []
    predef_apartments(V)
    assert calculate_expenses_by_type("gas", V) == 100

###### TESTING ############ 
test_create_apartment()
test_search()
test_sum()
test_max()
test_sort()
test_filter()
test_undo()

test_add()
test_replace()
test_remove()

test_calculate_expenses()
test_calculate_expenses_by_type()