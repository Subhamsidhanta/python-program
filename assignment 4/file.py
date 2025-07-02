try:
    with open("sample.txt","r") as f:
        lines=f.read()
        print("reading file content:")
        print(lines)
except Exception as e:
    print("file •sample. txt'was not found.Error: The")