#compare 2 lists
#I'm going to want to do this to compare previous runs with current runs.
#This does it with complete lists, but I'm sure I can do it on a JSON file or portions of one, CSV etc., although I may be able to just run it on slices of
#the retailers outputs

#Find LIKE Items In 2 Lists

#list comprehension
def intersection1(list1, list2):
    return [val for val in list1 if val in list2]

#using sets
#WORD OF CAUTION
#Sets will remove duplicate values from both lists, so I likely will not want to do it even though it would be faster
def intersection2(list1, list2):
    return [val for val in set(list1) & set(list2)]

#Manual looping
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common







#Find UNLIKE Items In 2 Lists
#list comprehension

def difference(A,B):
    only_A = [a for a in A if a not in B]
    only_B = [b for b in B if b not in A]
    return only_A + only_B

difference([1,2,3,3,4,5],[2,4,6,7,8])

#using sets
#WORD OF CAUTION
#Sets will remove duplicate values from both lists, so I likely will not want to do it even though it would be faster
#not sure yet...

#manual looking
#not sure yet...

#using symmetric difference' function
def difference2(A,B):
    return list(set(A).symmetric_difference(set(B)))

difference2([1,2,3,3,4,5],[2,4,6,7,8])