'''
Testing of algorithms
'''


'''
from sorting.bubble_sort import bubble_sort

print("***Bubble Sort***")
print("input: " , [2, 92, 8, -4, 0])
print("output: " , bubble_sort([2, 92, 8, -4, 0]))
'''

'''
from sorting.selection_sort import SelectionSort

print("***Selection Sort***")
print("input: " , [2, 92, 8, -4, 0])
print("output: " , SelectionSort([2, 92, 8, -4, 0]))
'''
'''
from sorting.bubble_sort_opt import bubble_sort_opt

print("***Bubble Sort Optimizado***")
print("input: " , [2, 92, 8, -4, 0])
print("output: " , bubble_sort_opt([2, 92, 8, -4, 0]))
'''
'''
from sorting.insertion_sort import insertion_sort

print("***Insertion Sort***")
print("input: " , [2, 92, 8, -4, 0])
print("output: " , insertion_sort([2, 92, 8, -4, 0]))
'''
'''
from unittest import result
from searching.binary_search import binary_search

print("***Binary Search***")

print("input: " , [2, 92, 8, -4, 0])
print("output: " , binary_search([2, 92, 8, -4, 0] , 0))

if result == -1:
    print("Ele elemento no se encontró")
else:
    print("El elemento está presente en la casilla: ", str(result))
'''
'''
from searching.linear_search import linear_search

print("***Linear Search***")
print("input: " , [2, 92, 8, -4, 0])
print("output: " , linear_search([2, 92, 8, -4, 0] , 8))
'''
'''
from recursion.factorial_of_n import fact

print("***Factorial de n***")
print("El factorial es: " , fact(6))
'''
'''
from recursion.countdown import regresive

print("***Cuenta regresiva***")
print(regresive(10+1))
'''
'''
from recursion.fibonacci_n import fibonacci

print("***Fibonacci***")
print(fibonacci(10))
'''
'''
from recursion.sum_of_n import sum

print("***suma de los primeros n numeros***")
print(sum(10))
'''
'''
from force_brute.pin_unlock import unlock

print("***Pin unlock***")
print(unlock("1923"))
'''
'''
from force_brute.divisors_of_n import divisores

print("***Divisores de n***")
n = 381
result = divisores(381)
print("n: " + str(n) + " divisors: " + str(result))
'''
'''
from force_brute.sum_of_first_n import suma
print("***suma de los primeros n numeros***")
print(suma(10))
'''
'''
from lists.list_merger import combinar

print("***List merge***")
combinar()
'''
'''
from lists.largest_number_in_list import maximo
print("***largest number***")
maximo()
'''