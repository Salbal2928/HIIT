# This program works by getting the full string
# and then using list slicing slices the full string
# to get the new desired string that is 
# "object-oriented programming with python"




message = "python is an interpreted, interactive, object-oriented programming language that combines remarkable power with ver clear syntax"

sliced_1 = message[39:67]
sliced_2 = message[107:112]
sliced_3 = message[0:7]

new_string = sliced_1 + sliced_2 + sliced_3
print(new_string)
