n = int(input())
array = [input() for i in range(n)] 
print("Yes") if array.count("For")*2>=n else print("No")
