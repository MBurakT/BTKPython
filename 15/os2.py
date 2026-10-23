import os

result = os.stat("os2.py")

result = os.path.abspath("os2.py")

result = os.path.dirname(os.path.abspath("os2.py"))

result = os.path.exists("os2.py")

print(result)

