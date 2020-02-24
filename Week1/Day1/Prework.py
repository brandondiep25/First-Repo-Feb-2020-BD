# Prework Question 1
def display_name(name):
    print (name)

Display("Brandon")

#Prework Question 2 -- Print 100 Odd Numbers 
def print odd ():
    for num in range (1, 101):
        if num % 2 !=0:
            print (num)

#Prework Question 3 - Find Max Number in a List
def max_num_in_list (a_list):
    max = a list[0]
    for a in a_list:
        if a > max:
            max = a
            return max

#Prework Question 3.a
def max_num(a_list):
    return max(a_list)

#Prework Question 4 - Function That Returns Leap Year for Given Year 
def is_leap(year):
    if year % 4 is == 0 and (year) % 400 == 0 or year % 100 ! =0):
        print('True')
    else:
        print ('False')

#Prework Question 5 -- Check if Numbers are Consecutive in a List
def is_consecutive(a_list):
    total = 2
    while total > 1:
        test = a_list.pop(0)
        if test == a_list[0] - 1:
            total = len(a_list)
        else:
            return False 
    return True

    def isconsec(a_list):
        for i in range(1, len(a_list)):
            if a_list[i] - 1!=a_list[i - 1]: 
                return False
            return True

# [4,5,6,7]