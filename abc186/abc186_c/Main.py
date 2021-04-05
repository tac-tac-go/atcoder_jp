n = int(input())
oct_v = [i for i in range(1,n+1) if "7" in oct(i)]
ten_v = [i for i in range(1,n+1) if "7" in str(i)]
print(n-len(set(oct_v+ten_v)))