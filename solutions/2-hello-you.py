#! python3

import sys

if len(sys.argv) > 1:
    subject = " and ".join(sys.argv[1:])
else:
    subject = "you"

print(f"Hello, {subject}!")
