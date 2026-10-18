class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass

VALID_AGE = 18
pin_code, balance, age = (int(x) for x in input().split(', '))

while True:
    line = input()

    if line == 'End':
        break

    parts = line.split('#')
    command = parts[0]

    if command == 'Send Money':
        money, pin = [int(x) for x in parts[1:]]
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < VALID_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif command == 'Receive Money':
        salary = int(parts[1])
        if salary < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        money = salary * 0.5
        balance += money
        print(f"{money:.2f} money went straight into the bank account")
