inp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sample = []
for i in range(len(inp)):
    i = sample[-1][-1] if sample else i
    for k in range(i+1, len(inp)):
        if inp[i] == 0:
            break
        if inp[i] <= inp[k]:
            sample.append((i, k))
            break
        elif k == len(inp)-1:
            i += 1
            sample.append(("D", i))
            break
intervals = [i for i in sample if "D" not in i]
h, t = intervals[0][0], intervals[0][-1]
count = 0
for i in intervals:
    for k in inp[i[0]:i[-1]]:
        count += (inp[i[0]] - k)
    # if (i > inp.index(h)) and (i < inp.index(t)):
    #     count += (h - inp[i])
print(count)

