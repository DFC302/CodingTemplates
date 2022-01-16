```
import sys
import os

Reference: https://stackoverflow.com/questions/35247817/is-there-a-way-for-a-python-script-to-know-if-it-is-being-piped-to

# 0 is file descriptor for input to program. 
# if 0 is not detected, then we know the input is not piped
if not os.isatty(0):
    for line in sys.stdin:
        line = line.strip("\n")

        print(line)

# if not stdin.... 
else:
    print("Not using standard in")
