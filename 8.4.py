## Justin Spencer Smith
## November 09, 2024
## SITD

fh = open(fname)
lst = list()


for line in fh:
    
    words = line.split()

    for word in words:

        if word not in lst:
            lst.append(word)
lst.sort() 

print(lst)
