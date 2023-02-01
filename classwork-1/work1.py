"""
this program takes in a string an returns the reverse of the 
the string using list slicing
 """
def reverse_string(msg):
    return msg[::-1]

msg = "ronaldo"
print("Initial string:", msg)
print("Reversed string:", reverse_string(msg))