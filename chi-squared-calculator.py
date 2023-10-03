from math import *
from data import *


def get_chi_squared():
    total = 0
    for x_set in colonization_categories:
        for y_set in poverty_categories:
            cell_value = 0
            for elem in range(len(x_set)):
                if x_set[elem] == "TRUE" and y_set[elem] == "TRUE":
                    cell_value += 1
            colonialism_value = 0
            for elem in x_set:
                if elem == "TRUE":
                    colonialism_value+=1
            poverty_value = 0
            for elem in y_set:
                if elem == "TRUE":
                    poverty_value += 1
            expected = colonialism_value*poverty_value/159
            total += (cell_value-expected)**2/expected
    return total

def P(a, b):
    intersection = 0
    for val in range(len(a)):
        if a[val]=="TRUE" and b[val]=="TRUE":
            intersection+=1
    intersection/=159
    P_b = 0
    for val in range(len(b)):
        if b[val]=="TRUE":
            P_b+=1
    P_b /= 159
    return intersection/P_b

def intersection(a, b):
    intersection = 0
    for val in range(len(a)):
        if a[val] == "TRUE" and b[val] == "TRUE":
            intersection += 1
    return intersection

print(P(more_than_twentyfive, has_been_colonized))
print(P(more_than_twentyfive, has_partially_been_colonized))
print(P(more_than_twentyfive, has_not_been_colonized))
print(P(more_than_twentyfive, is_europe))
