#sums numbers from 1 to n
print("\nA program to sum the number of integers from 1 to a given number n")
n = int(input("Enter a number: "))
n_list = []
n_sum = 0
for z in range(1,n+1):
    n_sum = n_sum + z
    n_list.append(z)
    z+=z
print(n_sum)




################################
#sums numbers from integer list
print("\nA program which sums the contents of an integer list or array")


#using integers from 1 to n from above
print("Using integers from 1 to n from above")
print(n_list)
int_sum = 0
for x in range(len(n_list)):
    int_sum = int_sum + n_list[x]
    x+=1
print(int_sum)




#using integers from input
print("\nUsing integers from input")
c = input("Enter list of numbers separated by space:")
print(list(c.split(' ')))
n_list = [int(f) for f in list(c.split(' '))]

int_sum = 0
for x in range(len(n_list)):
    int_sum = int_sum + n_list[x]
    x+=1
print(int_sum)





####################################
#translate given while loop to for loop
print("\nChange WHILE loop to FOR loop")
print("WHILE loop")
i = 20
while (i > 0):
    print("i =",i)
    i-=1

print("\nFOR loop")
i = 20
for b in range(i):
    print("i =",i)
    i-=1

