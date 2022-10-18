set1={3,3,4,5,6,7,2,1,7}
set2={9,7,6,4,3,2,7,8}

# set3=set1 | set2  #use for union of set
set3=set1.union(set2) #use for union of set
print(set3)

#intersection
# set4=set1&set2
set4=set1.intersection(set2)
print(set4)

set6={5,6,7}
set7={1,2,3}
set9=set6-set7
print(set9)