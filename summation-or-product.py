#Summation or Product

user_number = input("Enter a number: ")
user_number=int(user_number)

newlist= list(range(1,user_number+1))
print(newlist)


summation = sum(newlist)



print("Do you want to Sum or Multiply?")
user_choice = input()
if user_choice == "Sum":
    print(summation)
elif user_choice=="Multiply":
        i = 1
        while i < user_number :
            newlist[1] = newlist[0] * newlist[1]
            newlist.pop(0)
            if i == user_number - 1 :
                lastvalue=newlist.pop(0)
                print(lastvalue)
            i += 1
else:
    print("Please input 'Sum' or 'Multiply' only")

