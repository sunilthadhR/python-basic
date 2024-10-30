
ab = {"a": 100, "b": 200, "c": 100, "d": 100, "e":500, 'f':200, 'g':300, 'h':300}
cc = {}
keys = [i for i in ab.keys()]
values = [i for i in ab.values()]
li = []
for i in range(len(values)):
    if values[i] == -1:
        continue
    count = values[i]
    for j in range(i+1, len(values)):
        if values[i] == values[j]:
            count += values[i]
            values[j] = -1
            keys[j] = -1
    li.append(count)
keys = [i for i in keys if i!=-1]
cc = {k:v for k, v in zip(keys, li)}
print(cc)