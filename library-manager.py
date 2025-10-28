library = {
    "python basics": 5,
    "AI for beginners": 3,
    "DS 101": 4
}

library["Machine learning"] = 6
library["python basics"] = 8
library.pop("AI for beginners")

print(library)

if "DS 101" in library:
    print("Course Available")

print("Number of book titles:", len(library))