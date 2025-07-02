# 📁 File Handling Tasks – Python

This project demonstrates basic file operations in Python: **reading**, **writing**, and **appending** using two tasks.

---

## ✅ Task 1: Read a File with Exception Handling

**Description**:  
This task attempts to open and read the contents of a file named `sample.txt`.  
If the file does not exist, it handles the exception gracefully.

### 🔹 Features:
- Opens a file in read mode (`r`)
- Displays the content of the file
- Handles `FileNotFoundError` or any unexpected error using `try-except`

### 🧾 Sample Code:
```python
try:
    with open("sample.txt", "r") as f:
        lines = f.read()
        print("Reading file content:")
        print(lines)
except Exception as e:
    print("File 'sample.txt' was not found. Error:", e)
```

---

## ✅ Task 2: Write and Append to a File

**Description**:  
This task allows the user to:
1. Write initial input to a file called `output.txt`
2. Append more content to the same file
3. Read and display the final contents

### 🔹 Features:
- Uses write mode (`w`) to write user input
- Uses append mode (`a`) to add more text
- Uses read mode (`r`) to show final content

### 🧾 Sample Code:
```python
# Step 1: Write
text = input("Write to the file: ")
with open("output.txt", "w") as f:
    f.write(text + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append
append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(append_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display
print("Final content of output.txt:")
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
```
