students_data = {
    "shijo" : {
        "roll_number" : 431,
        "gender" : "male",
        "marks" : {"phy" : 89 , "chem" : 92 , "maths" : 99}
    },
    "Mayank" : {
        "roll_number" : 122,
        "gender" : "male",
        "marks" : {"phy" : 92, "chem" : 99 , "maths" : 96}
    },
     "Shashank" : {
        "roll_number" : 54,
        "gender" : "male",
        "marks" : {"phy" : 91 , "chem" : 78 , "maths" : 78}
    },
}

for k1 , v1 in students_data.items():
    for k2,v2 in students_data[k1]['marks'].items():
        print(k1 , k2 , v2)