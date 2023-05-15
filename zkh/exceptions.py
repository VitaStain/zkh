from rest_framework.exceptions import ValidationError


class EmailAlreadyExistsException(ValidationError):
    default_detail = "User with this email already exists"


class PasswordsDoNotMatchException(ValidationError):
    default_detail = "Passwords don't match"
