
file_Name = input("Enter the file to check: ").rstrip()
infile = open(file_Name, "r")
outfile = open("ga_sorted.txt", "w+")
content = []

for line in infile:
    content += line.strip().split()
    content = sorted([z.lower() for z in content])

outfile = open("ga_sorted.txt","a+")

with outfile as infile:
    for x in content:
        outfile.write("{}\n".format(x))
 
outfile.close

    


