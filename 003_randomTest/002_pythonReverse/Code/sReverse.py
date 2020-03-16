a = input("Enter a String:")

print("Orignal string:%s"%a)
print("Reverse string:%s"%a[::-1])

with open(r"C:\Users\keths\Desktop\Output.txt", "w") as text_file:
    print("Orignal string:%s"%a,file=text_file)
    print("Reverse string:%s"%a[::-1],file=text_file)