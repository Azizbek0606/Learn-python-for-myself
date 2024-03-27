s, s0 = "HelloWorldWorld", "World"
if s0 in s:
    idx = s.rfind(s0)
    s = s[:idx] + s[idx + len(s0) :]
print(s)
