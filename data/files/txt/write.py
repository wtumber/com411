def search(file_name):
    print("Searching...")
    sections = []
    books = []
    with open(file_name) as file:
        for line in file:
            if line.split(":")[0] == "Section":
                sections.append(line)
            else:
                books.append(line)
        print("Done")
    return (sections,books)

def save(file_name,data=("a","b")):
    print("Saving...")
    with open(file_name, "w") as file:
        file.write("Sections:{} \nBooks:{}".format(data[0],data[1]),end="")
    print("Done")

def run():
    print("running")
    data = search("books.txt")
    save("Section_books.txt",data)

run()