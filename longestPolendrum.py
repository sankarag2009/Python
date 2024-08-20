
class Solution2:
    def Poly(self, s:str):
        res=""
        reslen=0
        for i in range(len(s)-1):
            for j in [0,1]:
              l,r=i, i+j
              while l>=0 and r<len(s) and s[l]==s[r]:
                    if(r-l+1) > reslen:
                        res=s[l:r+1]
                        reslen=r-l+1
                    l -= 1
                    r += 1

        return res
if __name__=='__main__':
    a=Solution2()
    print(a.Poly('ipipipoiasdfdsareteyy'))
