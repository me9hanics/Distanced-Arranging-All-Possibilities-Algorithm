def Placing(arrangement, numbers):
    if 0 in arrangement:
        for element in range(len(arrangement)):
            if 0 == arrangement[element]:
                for number in numbers:
                    pair = element + number + 1
                    if pair < len(arrangement) and 0 == arrangement[pair]:

                        newArrangement = arrangement.copy() #don't modify the original arrangement
                        newArrangement[element] = number
                        newArrangement[pair] = number

                        newSet = numbers.copy()
                        newSet.remove(number)
                        
                        Placing(newArrangement, newSet)

                break
    else:
        print("A correct arrangement: ", *arrangement)

def AllArrangements(n):
    arrangement = [0] * 2 * n
    numbers =  list(range(1,n+1))
    Placing(arrangement, numbers)

#There will only be solutions for numbers with a remainder of 0 or 3 when divided by 4.
AllArrangements(1) # 0 solutions
AllArrangements(2) # 0 solutions
AllArrangements(3) # 2 solutions (one, and its mirror)
AllArrangements(4) # 2 solutions (one, and its mirror)
#AllArrangements(7) # Should be 52 solutions
#AllArrangements(8) # Should be 300 solutions
#AllArrangements(11) # A lot of solutions
#AllArrangements(12) # -||-
print("Done")