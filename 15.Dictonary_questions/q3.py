details = {
    "shijo": [90,80,70,80,90],
    "Jim" : [20,30,40,50,60],
    "Tom" : [20,80,70,67,33],
    "Jack": [50,60,65,75,86]
}

total = 0
for key in details:
    total = sum(details[key])
    print(total)