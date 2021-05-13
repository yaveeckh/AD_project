import numpy as np

import test

def levenshtein_distance_recursive(str1,str2):
    """complete this function"""
    if str1 == "":
        return len(str2)
    if str2 == "":
        return len(str1)
    if str1[-1] == str2[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([levenshtein_distance_recursive(str1[:-1], str2)+1,
               levenshtein_distance_recursive(str1, str2[:-1])+1, 
               levenshtein_distance_recursive(str1[:-1], str2[:-1]) + cost])
    return res

def levenshtein_distance_DP(str1,str2):
    """complete this function"""
    i = len(str1) + 1
    j = len(str2) + 1
    ld_matrix = np.zeros((i, j))
    for x in range(i):
        for y in range(j):
            if (x == 0):
                ld_matrix[0][y] = y
            elif (y == 0):
                ld_matrix[x][0] = x
            else:
                if str1[x-1] == str2[y-1]:
                    ld_matrix[x,y] = min(ld_matrix[x-1, y-1], ld_matrix[x, y-1]+1, ld_matrix[x, y-1] + 1)
                else:
                    ld_matrix [x,y] = min(ld_matrix[x-1, y-1] + 1, ld_matrix[x-1, y] + 1, ld_matrix[x, y-1] + 1)
    return (ld_matrix[i - 1, j - 1])