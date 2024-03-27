n = 5
s = "HelloWorld"
if len(s) > n:
    s = s[:n]
else:
    s += "." * (n - len(s))
print(s)
