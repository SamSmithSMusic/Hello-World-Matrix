import time

helloText = "Hello World!"

charset = [chr(i) for i in range(32, 127)]

# Initialize the current display as empty
currentText = [" "] * len(helloText)

#Find the write chars by both indexes
for i, targetChar in enumerate(helloText):
    while currentText[i] != targetChar:
        for char in charset:
            currentText[i] = char
            print("".join(currentText), end="\r")
            time.sleep(0.0035)
            if char == targetChar:
                break

print("".join(currentText))
input()