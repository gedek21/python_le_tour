import os
import sys

path = os.path.dirname(sys.executable)
print("KENDRIK LAMAR DAMN ALBUM IS 7 FROM ANTHONY FANTANO\nWTF")
print(path)

num = 1

while num <= 10:  
    print(num)
    num += 1



with open('poem.txt', encoding='utf8') as poem:
    for line in poem:
        print(line.strip())

