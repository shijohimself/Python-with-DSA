students_data = {
    "shijo" : {
        "roll_number" : 431,
        "gender" : "male",
        "marks" : [78,89,72,63,57]
    },
    "Mayank" : {
        "roll_number" : 122,
        "gender" : "male",
        "marks" : [83,45,68,23,45]
    },
     "Shashank" : {
        "roll_number" : 54,
        "gender" : "male",
        "marks" : [99,97,96,87,91]
    },
}

for names , details in students_data.items():
    total = sum(details["marks"])
    print(names , total)