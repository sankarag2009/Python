class CountSubstring:
    def countsubstrings(self, s:str):
        result=0
        for i in range(len(s)):
            for j in [0,1]:
                l, r=i, i+j
                print(s[i])
                while l>=0 and r < len(s) and s[l]==s[r]:
                    result += 1
                    l-=1
                    r+=1
        return result
    
if __name__=='__main__':
    s=CountSubstring()
    print(s.countsubstrings('dsferwerer'))
    print("this is last line")

