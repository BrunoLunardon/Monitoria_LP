def number_phone_br(number):
    if type(number) == str:
        number = number.replace('(', '')
        number = number.replace(')', '')
        number = number.replace(' ', '')
        number = number.replace('+55', '')
        number = number.replace('-', '')
        number = int(number)
        if str(number)[0:2] != '21':
            number = int('21' + str(number))
    return number

print(number_phone_br("99876-5432"))