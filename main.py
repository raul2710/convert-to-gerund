
import convert_to_gerund as ctg

print("Type a dot (.) to stop software")

while 1:
    verb = input("Type a verb to convert to gerund: ")
    if verb == ".":
        break
    print(ctg.transformVerbToIngForm(verb))