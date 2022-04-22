pattern = {
	"b":"d",
  	"d":"b",
  	"p":"q",
  	"q":"p"
}
s_c = input()
s = s_c[::-1]
result = [pattern[i] for i in s]
print("Yes") if "".join(result)==s_c else print("No")
