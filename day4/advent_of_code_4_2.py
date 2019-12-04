valid_count = 0

password = 367479

while password <= 893698:
    string_password = str(password)
    digits = [int(string_password[0]), int(string_password[1]), int(string_password[2]), int(string_password[3]), int(string_password[4]), int(string_password[5])]
    #check each digit is less than the next besides the last
    number_is_valid = True
    for i in range(0, len(digits) - 1):
        if digits[i] > digits[i + 1]:
            number_is_valid = False

    if number_is_valid:
        not_valid_numbers = []
        number_has_a_pair = False
        for number in range(10):
            for i in range(0, len(digits) - 1):
                if digits[i] == number and digits[i + 1] == number and number not in not_valid_numbers:
                    if i < 4:
                        if digits[i + 1] == number and digits[i + 2] == number:
                                not_valid_numbers.append(number)
                        else:
                            number_has_a_pair = True
                    else:
                        number_has_a_pair = True
        if number_has_a_pair:
            valid_count += 1

    password += 1

print(valid_count)