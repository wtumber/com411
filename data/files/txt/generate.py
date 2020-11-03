def search(filename):
    print("Searching")
    data = {}
    with open(filename) as file:
        section_name= ""
        for line in file:
            if line.startswith("Section"):
                parts= line.split(":")
                section_name = parts[1].strip()
            else:
                if section_name in data:
                    values = data[section_name]
                    values.append(line.strip())
                else:
                    data[section_name] = line.strip()
    return data

def run():
    data = search("books.txt")
    with open("gen.csv","w") as file:
        for item in data.items():
            section = item[0]
            books = item[1]
            for book in books:
                file.write(f"{section},{book}\n")

run()





#c:/Users/ISA06006086/Documents/Code/Uni/com411/data/files/txt
