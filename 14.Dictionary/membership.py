from typing import Dict
marks: Dict[str,int] = {
    "history" : 90,
    "maths" : 100,
    "sst" : 70,
    "hindi" : 89,
    "english" : 94
}

print(100 in marks) # bcoz there is no key with name 100
print("maths" in marks)