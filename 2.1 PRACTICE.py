def is_isogram(input_string):


input_string = input_string.lower()




unique_chars = set()




for char in input_string:


if char in unique_chars:
return False




unique_chars.add(char)




return True


print(is_isogram("isogram"))
print(is_isogram("uncopyrightable"))
print(is_isogram("ambidextrously"))
print(is_isogram("people"))
print(is_isogram("chinyere"))
print(is_isogram("juice"))
