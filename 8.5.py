## Justin Spencer Smith
## November 09, 2024
## SITD


fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

count = 0

for line in fh:
    address = line.strip()
    if address.startswith('From '):
        count += 1

print("There were", count, "lines in the file with From as the first word")
