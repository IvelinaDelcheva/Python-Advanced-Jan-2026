class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_NAME_LENGTH = 5
VALID_DOMAINS = ['com', 'bg', 'net', 'org']

while True:
    line = input()

    if line == "End":
        break

    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = line.split("@")

    if len(name) < VALID_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain.split(".")[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


