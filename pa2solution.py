from __future__ import print_function
# in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random

# NAME: Gannon Faul 
# STUDENT ID NUMBER: 101713237
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: Gannon Faul


def free_time_intervals(interval_lst, T):
    # First design the algorithm on pen/paper before you attempt this
    sorted_lst = sorted(interval_lst, key=lambda tup: tup[0])

    i = 0
    while i < len(sorted_lst):
        if i + 1 < len(sorted_lst) and sorted_lst[i][1] >= sorted_lst[i + 1][0]:
            if sorted_lst[i][1] < sorted_lst[i + 1][1]:
                sorted_lst[i] = (sorted_lst[i][0], sorted_lst[i + 1][1])
                del sorted_lst[i + 1]
                i -= 1
            else:
                del sorted_lst[i + 1]
                i -= 1
        i += 1        

    time = [0 for i in range(T+1)]

    for i in range(len(sorted_lst)):
        lower = sorted_lst[i][0]
        higher = sorted_lst[i][1]
        if lower <= T:
            time[lower] = 1
        else:
            break    
        if higher <= T:
            time[higher] = 3
        for j in range(lower + 1, higher):
            if j > T:
                break
            else:
                time[j] = 2

    free_intervals = []

    lower = 0
    higher = 0
    i = 0
    while i < T:
        if i == 0 and time[i] == 0:
            higher = 1
            while i < T - 1 and time[i + 1] == 0:
                higher += 1
                i += 1
            free_intervals.append((lower, lower + higher))
            i = lower + higher
        elif time[i + 1] == 0:
            lower = i
            higher = 1
            while i < T - 1 and time[i + 1] == 0:
                higher += 1
                i += 1
            free_intervals.append((lower, lower + higher))
            i = lower + higher
        elif time[i] == 3 and time[i+1] == 1:
            lower = i
            higher = i + 1
            free_intervals.append((lower, higher))
            i += 1
        i += 1

    return free_intervals

def max_logged_in(interval_lst,T):
    # First design the algorithm on pen/paper and solve a few examples.
    time = [0 for i in range(T+1)]

    for i in range(len(interval_lst)):
        lower = interval_lst[i][0]
        higher = interval_lst[i][1] + 1
        for j in range(lower, higher):
            if j > T:
                break
            else:
                time[j] += 1

    max_time = 0
    max_users = 0
    for i in range(T + 1):
        if time[i] > max_users:
            max_users = time[i]
            max_time = i

    result = (max_users, max_time)

    return result



if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input:', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
