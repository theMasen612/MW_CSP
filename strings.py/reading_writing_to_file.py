# VL, Reading and writing to file

with open( 'practice.txt', "r") as file:
    content = file.read()
    print(content)
    word = content.find("waldron")
    length = len("waldron")
    print(content.upper())
    print(content[word:word+length])
    

with open("print.txt", "w") as file:
    file.write("hello")