from random import choices

f=open("data.txt")
s=f.read()
l=s.split(" ")x
d = {}

for i in range(len(l)-1):
    x=l[i]
    y=l[i+1]
    if x in d:
        if y in d[x]:
            d[x][y]+=1
        else:
            d[x][y]=1
    else:
        d[x]={y:1}

result=["Я"]
for i in range(1000):
    matches = d[result[-1]]
    sorted_words = sorted(matches, key=matches.get)
    weights = [1/(i+1) for i in range(len(sorted_words))]
    result.append(choices(sorted_words, weights=weights)[0])

print(" ".join(result))

