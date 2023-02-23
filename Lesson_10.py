# Lesson 10 Day 10
# Function with outputs
def format_name(first_name, last_name):
    """
        This function take a first and
        last name and return the title
        case version of the name.
    """
    format_f_name = first_name.title()
    format_l_name = last_name.title()

    return f"{format_f_name}, {format_l_name}"


f_name = input("Please enter your firstname: ")
l_name = input("Please enter your lastname: ")
format_string = format_name(first_name=f_name, last_name=l_name)
print(format_string)


