X = int(input())
div,mod = divmod(X,500)
mod = mod //5
print(1000*div+5*mod)