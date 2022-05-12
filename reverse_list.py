#Author: Faith Elledge
#Grithub user: Elledgef
#Date: 5/11
#Description: Reverses order of numbers in orginal list

def reverse_list(lst):
    for i in range(len(lst)//2):
        lst[i],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[i]