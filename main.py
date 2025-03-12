from random import randint

arr = ["Rock", "Paper", "Scissor"]

r = randint(0,2)
print ("Enter: ")
for i in range(3):
    print("\t",i+1,"-",arr[i])
u = int(input("-> "))

print("Robot selected "+arr[r])
print("User selected "+arr[u-1])

if(r == u-1):
    print("Game tied")
elif(r == u%3):
    print("Robot wins")
else:
    print("User wins")