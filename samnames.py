#open boy name file

infile = open("BoyNames.txt")

#create set

boyNames = set()

#iterate through file

for bname in infile:

    #right strip each name and add it to the set

    boyNames.add(bname.rstrip())

#close file

infile.close()

 

#open girl name file

infile = open("GirlNames.txt")

#create set

girlNames = set()

#iterate through file

for gname in infile:

    #right strip each name and add it to the set

    girlNames.add(gname.rstrip())

#close file

infile.close()

 

#print unisex names:

print("Unisex names:")

#iterate through the names that are in both sets

for name in boyNames.intersection(girlNames):

    #print name

    print(name,end=" ")