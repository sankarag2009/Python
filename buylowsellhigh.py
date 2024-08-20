s=[1,2,3,4,5,5,8,9,1,3,4,1,25]
def buylowsellhigh(s:list):
    l, r=0, 1
    maxprofit=0
    while r <= len(s)-1:
        if (s[r]-s[l]>0):
            if(s[r]-s[l]> maxprofit): 
                maxprofit=s[r]-s[l]
                print(maxprofit)            
        else:
            l=r
        r+=1
    return maxprofit

print(buylowsellhigh(s))