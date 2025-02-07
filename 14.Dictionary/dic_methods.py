from typing import Dict
marks: Dict[str,int] = {
    "history" : 90,
    "maths" : 100,
    "sst" : 70,
    "hindi" : 89,
    "english" : 94
}

print(marks)
# marks.clear()
# print(marks)

# print(marks["historyyy"]) # key-error
print(marks.get("historyyy",0))
# by default -> none we can change that to anything

marks.pop("sst")
print(marks)

dict_1 = {"a" : 1 , "b" : 2}
dict_2 = {"c" : 3 , "d" : 4 , "a" : 100}

dict_1.update(dict_2)
print(dict_1)