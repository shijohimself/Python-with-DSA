# longest word in given string
# *********** revise this question!
mystr = "Batman killed Superman in gothamcitycentre"

longest = ""
current = ""

for ch in mystr:
    if ch == " ":
        if len(current) > len(longest):
            longest = current
        current = ""
    else:
        current += ch
if len(current) > len(longest):
    longest = current
print(longest,current)