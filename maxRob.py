
class Solution:
    def maxrob(nums:list[int])->int:
        rob1, rob2 = 0, 0
        for i in nums:
            rob1, rob2 = rob2, max(rob1+i, rob2) 
        return rob2    
if __name__ == '__main__': 
    a=Solution
    print(a.maxrob([2,7,9,3,1,10,23,17]))
    print(a.maxrob([2,3,2]))

# explanation 
# rob1=0 , rob2=0
# rob1=0 rob2=max(0+2, 0)=2
# rob1=2 rob2=max(0+7, 2)=7
# rob1=7, rob2=(2+9, 7)=11
# rob1=11, rob2=(7+3, 11)=11
# rob1=11, rob2=(11+1, 11)=12
# rob1=12, rob2=(11+10, 12)=21
# rob1=21, rob2=(21+17, 21)=38
#loop ends and retur rob2 which holds greatest value always

