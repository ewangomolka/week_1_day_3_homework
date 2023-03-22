def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string( test_string ):
    return len(test_string)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number( string_1, string_2):
    # return int(string_1) + int(string_2)
    return add(int(string_1), int(string_2))

def number_to_full_month_name( month ):
    if month == 1:
        return "January"
    elif month == 2:
        return "Febuary"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        return None

def number_to_short_month_name( month ):
    if month == 1:
        return "Jan"
    elif month == 2:
        return "Feb"
    elif month == 3:
        return "Mar"
    elif month == 4:
        return "Apr"
    elif month == 5:
        return "May"
    elif month == 6:
        return "Jun"
    elif month == 7:
        return "Jul"
    elif month == 8:
        return "Aug"
    elif month == 9:
        return "Sep"
    elif month == 10:
        return "Oct"
    elif month == 11:
        return "Nov"
    elif month == 12:
        return "Dec"
    else:
        return None
    
def length_of_cube( int_1 ):
    return int_1 * int_1 * int_1

def string_1( string ):
    str = ""
    for i in string:
        str = i + str
    return str

def temprature( temp ):
    result = (temp - 32) * (5/9)
    return round(result, 2)