inp="aaaabbbccdddeeddsaj"
inp=list(inp)
print(inp)
d={}.fromkeys(inp,0)
c=1
print("unique Values",d)
for p in inp:
    if p in d:
        d[p]=d[p]+1
for q,r in d.items():
    print("{}-{}".format(q,r),end="")

