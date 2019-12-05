
def password_combinations(lower, upper):
    total = 0
    for number in range(lower, upper + 1):
        if check_combination_valid(number):
            total += 1
    return total


def check_combination_valid(number):
    str_num = str(number)
    for i in range(len(str_num) - 1):
        cur_num = str_num[i]
        if str_num[i] == str_num[i + 1]:
            if (i == 0 or str_num[i - 1] != cur_num) and (i == (len(str_num) - 2) or str_num[i + 2] != cur_num):
                break
    else:
        return False

    for i in range(len(str_num) - 1):
        if int(str_num[i]) > int(str_num[i + 1]):
            return False

    return True


print(password_combinations(254032, 789860))