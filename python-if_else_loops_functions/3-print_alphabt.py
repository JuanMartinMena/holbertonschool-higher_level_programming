#!/usr/bin/python3
result = ""
for i in range(99):
    result += "{} = 0x{:x}\n".format(i, i)
print(result, end="")
