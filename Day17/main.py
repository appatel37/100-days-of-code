with open("data.txt", "w") as file:
    file.write("Day 17 - File Handling Practice\n")
    file.write("Learning how to read and write files\n")
    file.write("Python makes it easy!\n")

print("File written successfully!\n")

with open("data.txt", "r") as file:
    content = file.read()
    print("File contents after writing:\n")
    print(content)

with open("data.txt", "a") as file:
    file.write("Appended line successfully!\n")

print("\nNew line appended successfully!\n")

with open("data.txt", "r") as file:
    updated_content = file.read()
    print("Final file contents:\n")
    print(updated_content)