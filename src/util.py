class UserInputError(Exception):
    pass

def validate_todo(content):
    if len(content) < 5:
        raise UserInputError("Todo content length must be greater than 4")

    if len(content) > 100:
        raise UserInputError("Todo content length must be smaller than 100")


def validate_year(year):
    if int(year) > 2024 or int(year) < 1:
        raise UserInputError("Vuoden tulee olla välillä 1-2024.")
    