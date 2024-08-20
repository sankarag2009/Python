
s='dhfreiewdndslkvnqweiurejtlknfaksdjiuewhriuhanfj'
s1='dhs'
dics1=dict()
maxVal=len(s)*2
minlenght=maxVal
for i in s1:
    dics1[i]=maxVal
for i, c in enumerate(s):
    if(c in s1):
        dics1[c]=i
        if(max(dics1.values())-min(dics1.values())+1) < minlenght:
            minlenght=max(dics1.values())-min(dics1.values())+1
            print(list(dics1.values()))
print("space")if minlenght > len(s) else print(f"minlengh{minlenght}")