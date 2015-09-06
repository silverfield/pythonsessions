# print positive integers up to 47 (excluding)
x = 1
while x < 47:
    print(x)
    x = x + 1

print("------------------------------------------")

# print all odd numbers up to 50
x = 1
while x < 50:
    if x % 2 == 1:
        print(x)
    x += 1  # concise way of incrementing x

print("------------------------------------------")

# example of a while loop where no iteration will be executed
while 1 == 0:
    print("this should never happen")

print("------------------------------------------")

# example of never-ending while loop
# while 1 == 1:
#     print("this is forever repeated")

print("------------------------------------------")

# will prompt the user for lines of input, put them to list and print the list at the end
print("Write several lines and terminate with stop (and ENTER). ")
l = []
inp = input()
while inp != "stop":
    l.append(inp)
    inp = input()  # be careful not to forget this line - the program will take on too much memory and slow down you PC
print("You've entered: " + str(l))  # concise way of printing a list

print("------------------------------------------")

# reads in numbers separated by space and computes their sum
s = input("Write numbers separated by space (no space after last one). At the end, press enter. ")
l = [int(i) for i in s.split(' ')]
print("The sum is: " + str(sum(l)))