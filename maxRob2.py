# in this case last element of the array is connected to first element of the array. If we consider
# first house to rob then we will have to gave up on last house, else we will have to gave up on first house
class Soluiton:
    def helprobFunciton(self, nums:list[int]):
        rob1, rob2=0,0
        for i in nums:
            rob1, rob2=rob2, max(rob1+i, rob2)
            return rob2
    def robFunction(self,nums:list[int]):
        print(nums[1:])
        print(nums[:-1])
        return max(self.helprobFunciton(nums[1:]), self.helprobFunciton(nums[:-1]))
if __name__=='__main__':
    a=Soluiton()
    print(a.robFunction([2,3,2]))
