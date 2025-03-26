def cyusa():
    try:
        filename = input("Enter file name: ")  
        with open(filename, "r") as file:
            data = file.read()
        
        user = input("\nSay anything: ") 
        with open("output.txt", "w") as file:
            file.write(data + "\n" + user)
        
        return "Changes saved to output.txt successfully."

    except FileNotFoundError:
        return "File not found. Please check the filename and try again."
print(cyusa())
