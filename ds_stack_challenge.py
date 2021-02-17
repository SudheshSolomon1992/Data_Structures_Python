import ds_stack

string = "hsehdus nomolos"
reversed_string = ''

s = ds_stack.Stack()

for char in string:
    s.push (char)

while not s.is_empty():
    reversed_string += s.pop()

print ("Reverse of given string is: ".format(reversed_string))