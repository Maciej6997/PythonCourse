
import os

#RELATIVE PATH FROM 
#C:\Users\Maciek\Desktop\nauka\python\PYTHON\Files, Paths
#to 
#C:\Users\Maciek\Desktop\plik.txt


path = "../../../../plik.txt"
full_path = os.path.abspath(path)
print(full_path)


with open(path) as file:
    content = file.read()
    print(content)


with open(full_path) as file:
    content = file.read()
    print(content)