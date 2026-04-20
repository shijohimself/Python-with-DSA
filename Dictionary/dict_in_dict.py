students_data = {
    "shijo" : {
        "roll_number" : 431,
        "gender" : "male",
        "physics" : 79,
        "chemistry" : 82,
        "maths" : 99,
    },
    "Mayank" : {
        "roll_number" : 122,
        "gender" : "male",
        "physics" : 93,
        "chemistry" : 82,
        "maths" : 59,
    },
     "Shashank" : {
        "roll_number" : 54,
        "gender" : "male",
        "physics" : 38,
        "chemistry" : 42,
        "maths" : 95,
    },
}

# print(students_data["shijo"])

# for names, details in students_data.items():
#     print(names , details)

for names , details in students_data.items():
    total = details["physics"] + details['chemistry'] + details["maths"]
    print(names)
    print(total)