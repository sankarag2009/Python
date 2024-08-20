class result:
    def numberofsteps(nums:int):
        one, two=1,1
        for i in range(nums-1):
            one, two=one+two, one
        return one
    
    # Driver program to test above functions. 
if __name__ == '__main__': 
    a=result
    print(a.numberofsteps(5))