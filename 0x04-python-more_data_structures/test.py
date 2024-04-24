strg = "Zainab"
flag = 1
for i in range (len(strg)):
    if not flag:
        flag = 1
        continue
    print (strg[i])
    if strg[i+1] == 'n':
        flag = 0
 