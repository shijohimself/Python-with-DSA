from typing import Dict
marks: Dict[str,int] = {
    "history" : 90,
    "maths" : 100,
    "sst" : 70,
    "hindi" : 89,
    "english" : 94
}

print(marks)

marks["sst"] = 100
marks["sanskrit"] = 90

# marks.update({"sanskrit": 89})
# marks.update({"maths":90})
print(marks)