def is_valid_parentheses(s):
    balance = 0

    for ch in s:
        if ch == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0