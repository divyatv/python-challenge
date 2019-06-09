newlist= [['Khan', [3521001, 2218231, 63.00001050837531]], ['Correy', [3521001, 70425500, 19.999994319797125]], ['Li', [3521001, 492940, 13.999996023857989]], ["O'Tooley", [3521001, 105630, 2.999999147969569]]]

print("what=", newlist[0][1][0])

for each in newlist:
    print ("each iterable=", each)
    #print ("name of candidate=", newlist[each][0])

print ("length of newlist=", len(newlist))    
votes=[]
for i in range(len(newlist)): 
    print ("name=", newlist[i][0])
    print (" votes for name", newlist[i][1][1])
    print (" percentage", newlist[i][1][2])
    votes.append(newlist[i][1][1]) 
print("voteslist=", votes)    
a=max(votes)
print(a)
index=votes.index(a)
print ("index=", index)
print("winner is in", newlist[index])
print ("name of winner",newlist[index][0] )


