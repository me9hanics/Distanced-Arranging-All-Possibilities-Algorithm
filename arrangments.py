def PlaceOne(arrangement, numbers):
    
    #if 0 in arrangement:
    #    for i in range(0,len(arrangement)):
    #        if 0 != arrangement.index(i):
    #            #algorithm to be implemented (recursive, forEach)
    #            #if() ... PlaceOne(arrangement, numbers)
    #else:
    #    print("A correct arrangement" + arrangement)
    return 0

def AllArrangements(n):
    arrangement = [0] * 2 * n
    numbers =  list(range(1,n+1))
    PlaceOne(arrangement, numbers)



AllArrangements(3)
AllArrangements(4)
#AllArrangements(7)
#AllArrangements(8)
#AllArrangements(11)
#AllArrangements(12)
print("Done")