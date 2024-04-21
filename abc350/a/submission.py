s = input()
bool = s in ["ABC"+str(i).zfill(3) for i in range(1,350)] and s!="ABC316"
print("Yes") if bool else print("No")
