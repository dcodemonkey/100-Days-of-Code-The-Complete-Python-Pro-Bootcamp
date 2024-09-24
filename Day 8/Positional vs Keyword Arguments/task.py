# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Jack Bauer")

# Functions with more than 1 input
# def greet_name(name, location):
#     print(f"Hi, {name}")
#     print(f"What is it like in {location}")
# greet_name("John Doe", "Nowhere")
# greet_name(location="New Delhi",name="Kunal")

def calculate_love_score(boy_name, girl_name):
    combined_name = boy_name + girl_name
    lower_names = combined_name.lower()

    t = lower_names.count('t')
    r = lower_names.count('r')
    u = lower_names.count('u')
    e = lower_names.count('e')
    num1 = t+r+u+e

    l = lower_names.count('l')
    o = lower_names.count('o')
    v = lower_names.count('v')
    e = lower_names.count('e')
    num2 = l+o+v+e

    final_score = int(str(num1) + str(num2))
    print(final_score)

calculate_love_score("kunal", "sapna")
