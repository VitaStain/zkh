from rest_framework.exceptions import ValidationError


class EmailAlreadyExistsException(ValidationError):
    default_detail = "User with this email already exists"


class PasswordsDoNotMatchException(ValidationError):
    default_detail = "Passwords don't match"


class ServiceDoesNotExistException(ValidationError):
    default_detail = "This service dose not exist"


class OrderDoesNotExistException(ValidationError):
    default_detail = "This order dose not exist"


class WorkerDoesNotExistException(ValidationError):
    default_detail = "This worker dose not exist"
