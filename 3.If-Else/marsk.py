"""
ask a mark from user 
91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
below 60 -> E
"""

marks_obtained = int(input("Total Marks obtained: "))

if marks_obtained >= 91 and marks_obtained <= 100:
    print("A")
elif marks_obtained >= 81 and marks_obtained <= 90:
    print("B")
elif marks_obtained >= 71 and marks_obtained <= 80:
    print("C")
elif marks_obtained >= 61 and marks_obtained <= 70:
    print("D")
elif marks_obtained >= 0 and marks_obtained <= 60:
    print("Fail")
else:
    print("Invalid")