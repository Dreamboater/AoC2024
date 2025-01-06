
f = open("Day 1 Input", "r")
sum = 0
pair = ""
list1 = []
list2 = []
for i in range(0,1000):
    pair = f.readline()
    pair = pair.split()
    list1.append(int(pair[0]))
    list2.append(int(pair[1]))

#Day 1 Part 1#
#.sort()
#list2.sort()
#print(list1)
#print(list2)
#for i in range(0,1000):
#    sum = sum + abs(int(list1[i])-int(list2[i]))
#print(sum)

#Day 2 Part 2#
#similarity = 0
#for s in list1:
#    similarity = similarity + s*list2.count(s)
#
#print(similarity)

