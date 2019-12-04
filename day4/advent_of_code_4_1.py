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

    number_was_counted = False
    if number_is_valid:
        for i in range(0, len(digits) - 1):
            if digits[i] == digits[i + 1]:
                valid_count += 1
                number_was_counted = True
                break
    
    password += 1

    #set the new password
    #password = int(f"{digits[0]}{digits[1]}{digits[2]}{digits[3]}{digits[4]}{digits[5]}") + 1

print(valid_count)
