ls = ['яблоко','персик','апельсин','мандарин','банан']

for ind, itm in enumerate(ls, start=1):
    if ind % 2 == 0 :
        ls[ind - 1] = 'четное'
        # print(ind, itm)
print(f"{'-'.join(ls)}")