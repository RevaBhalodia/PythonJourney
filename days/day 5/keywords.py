#break = loop will stop
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop.")

#continue = current ko skip kartna h like skip
i = 0
while i <= 6:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

