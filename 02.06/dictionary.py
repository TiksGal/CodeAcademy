# dictionary

countries_and_capitals = {
    "Lithuania" : "Vilnius",
    "Poland" : "Warsaw",
    "Latvia" : {
         "capital" : "Riga",
        "population" : "2000000",
    }  
    }

students = {
    "name" : "Antanas",
    "Age" : "20",
    "Surname" : "Antanaitis"
}


print(students["Age"])

print(students)

print(students.get("can", "money"))

print(countries_and_capitals["Latvia"]["population"])

print(list(countries_and_capitals.items()))

print(list(countries_and_capitals.keys()))

print(list(countries_and_capitals.values()))

print(countries_and_capitals)
countries_and_capitals.pop("Latvia")
print(countries_and_capitals)

new_country = {"Spain" : "Madrid","France" : "Paris"}
countries_and_capitals.update(new_country)
print(countries_and_capitals)