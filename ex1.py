def length_checker(max_length):
    def inner_function(input_text):
        if len(input_text) > max_length:
            raise ValueError(f'name length is bigger than {max_length}')
        return input_text
    return inner_function

@length_checker(10)
def validate_first_name(first_name):
    return first_name

@length_checker(10)
def validate_last_name(last_name):
    return last_name

def user_registration(first_name, last_name):
    try:
        validate_first_name(first_name)
        validate_last_name(last_name)
        print(f'{name} {family} registerd sucessfuly !!')
    except ValueError:
        print('Rregister not sucessfuly !')
user_input = input().strip()  # No prompt message
name, family = [item.strip() for item in user_input.split(',')]
user_registration(name, family)
