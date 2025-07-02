text = input("Write to the file: ")
with open("output.txt", "w") as f:
    f.write(text + "\n")
print("Data successfully written to output.txt.")

append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(append_text + "\n")
print("Data successfully appended.")

print("Final content of output.txt:")
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
