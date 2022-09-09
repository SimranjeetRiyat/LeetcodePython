import random
import string


class Solution:
    def strongPasswordChecker(password: str) -> int:
        pwd = [*password]
        lower_case = [*string.ascii_lowercase]
        upper_case = [*string.ascii_uppercase]
        digits = [*string.digits]
        count = 0

        if len(set(pwd).intersection(set(lower_case))) == 0:
            pwd.insert(0, random.choice(lower_case))
            count = count + 1
        if len(set(pwd).intersection(set(upper_case))) == 0:
            pwd.insert(0, random.choice(upper_case))
            count = count + 1
        if len(set(pwd).intersection(set(digits))) == 0:
            pwd.insert(0, random.choice(digits))
            count = count + 1

        if len(pwd) > 20:
            for i in range(len(pwd) - 20):
                if (
                    len(set(pwd).intersection(set(lower_case))) > 1
                    and pwd[i] in lower_case
                ):
                    del pwd[i]
                    count = count + 1
                if (
                    len(set(pwd).intersection(set(upper_case))) > 1
                    and pwd[i] in upper_case
                ):
                    del pwd[i]
                    count = count + 1
                if len(set(pwd).intersection(set(digits))) > 1 and pwd[i] in digits:
                    del pwd[i]
                    count = count + 1

        if len(pwd) < 6:
            for i in range(6 - len(pwd)):
                if pwd[-1] not in lower_case and len(pwd) < 6:
                    pwd.append(random.choice(lower_case))
                    count = count + 1
                if pwd[-1] not in upper_case and len(pwd) < 6:
                    pwd.append(random.choice(upper_case))
                    count = count + 1
                if pwd[-1] not in digits and len(pwd) < 6:
                    pwd.append(random.choice(digits))
                    count = count + 1

        if 6 <= len(pwd) <= 20:
            for i in range(len(pwd)):
                if i <= len(pwd) - 2 and pwd[i] == pwd[i + 1] == pwd[i + 2]:
                    if pwd[i].islower() == True:
                        pwd[i] = random.choice(lower_case)
                        count = count + 1
                    elif password.isupper() == True:
                        pwd[i] = random.choice(upper_case)
                        count = count + 1
                    elif password.isdigit() == True:
                        pwd[i] = random.choice(lower_case)
                        count = count + 1
                    elif (
                        pwd[i].islower() == False
                        and password.isupper() == False
                        and password.isdigit() == False
                    ):
                        pwd[i] = random.choice(digits)
                        count = count + 1
        return count, pwd

    print(strongPasswordChecker("aqwedvbgeslpqebcjitywedfh"))
