def get_multiplied_digits(number):
    if str(number).endswith('0'):
        str_number = str(number // 10)
    else:
        str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
