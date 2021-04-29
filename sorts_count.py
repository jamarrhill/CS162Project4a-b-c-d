# Name: Jamar Hill
# Date: 4/25/2021
# Description: CS 162 Project 4d

def insertion_count(1):
    comp_count = 0
    ex_count = 0
    for i in range(1,len(1)):
        current = 1[i]
        j = i - 1
        for k in range(j, -1, -1):
            comp_count += 1
            if current < 1[k]:
                1[k + 1] = 1[k]
                ex_count += 1
                k_last = k
            else:
                k_last = k + 1
                break

        1[k_last] =current
    return (comp_count, ex_count)


test_num_list = [10,9,8,7,6,5,4,3,2,1]

print(insertion_count(test_num_list))
