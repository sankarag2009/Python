class Solution:
    def minimumcost(costarray:list):
        costarray.append(0)
        for i in range(len(costarray)-3, -1, -1):
            costarray[i] += min(costarray[i+1],costarray[i+2])
        return min(costarray[0], costarray[1])
    


    # Driver program to test above functions. 
if __name__ == '__main__': 
   a=Solution
   print(a.minimumcost([10,15,20]))
   print(a.minimumcost([1,100,200,1,1,100,1,1,100,1, 0]))
   print(a.minimumcost1([10,15,20]))
   print(a.minimumcost1([1,100,200,1,1,100,1,1,100,1, 0]))