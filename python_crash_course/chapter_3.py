# Example 1
# alist = [1, 55, "Here we are"]
# blist = [356, 12, "month", ["jan", "feb", "mar"], 10000]
#
# print(alist)
# print(blist[3])

# Example 2
# numbers = [2, 4, 6, 8, 10]
# for a in numbers:
#     b = a+2
#     print(b, end=" , ")

# Example 3
# alist = [1, 55, "Here we are"]
# blist = [356, 12, "month", ["jan", "feb", "mar"], 10000]
#
# numbers = [2, 4, 6, 8, 10]
# for a in numbers:
#     b = a+2
#     print(b, end=(", "))
# print()
#
# xlist = alist[1:5]
# print(xlist)
# print(len(xlist))
# print(len(alist))
#
# ylist = blist+["april", "may", "june"]
# print(ylist)
# print(len(blist))
# print(len(ylist))

# Example 4
# create list with 3 colors
listz = ['red', 'green', 'blue']
print(listz)

# add to previous list 2 more colors
listm = listz + ["black", "white"]
print(listm)

# replace blue with yellow
listm[2] = "yellow"
print(listm)

# delete color green from second list
listm.remove("green")
print(listm)
listm.pop(0)
print(listm)

# Example 5
count = 1
while count <= 3:
    print(count," ",listm[count-1])
    count += 1

count = 1
while count <= 3:
    for i in listm:
        print(f'{count}\t{i.capitalize()}')
        count += 1
