S=input()
T=input()
edge=['AB','BC','CD','DE','EA','AE','ED','DC','CB','BA']
if S in edge and T in edge:
  print('Yes')
elif S not in edge and T not in edge:
  print('Yes')
else:
  print('No')
