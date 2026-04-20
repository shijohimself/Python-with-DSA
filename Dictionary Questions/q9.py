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

# for k , v in students_data.items():
#     print(k)
#     print(v["marks"])

for k , v in students_data.items():
    result = 0
    for m in v["marks"]:
        result += m
    print(k,result)