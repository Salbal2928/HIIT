def func(msg:str)->str:
    if len(msg) <= 2:
        return "string to short"
    new_msg = ""
    for i in range(0,2):
        new_msg += msg[i]
    for i in range(1,3):
        new_msg += msg[-i]
    return new_msg


print(func("salbal"))
