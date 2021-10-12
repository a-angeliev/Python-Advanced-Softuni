class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


line = input()

while not line == "End":
    if not "@" in line:
        raise MustContainAtSymbolError("Email must contain @")
    name, email = line.split("@")
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if not "." in email:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    left_part, right_part = email.split(".")
    if right_part != "com" and right_part != "bg" and right_part != "org" and right_part != "net":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    line = input()