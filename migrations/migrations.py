from credentials import APIKeys

new_keys = APIKeys('testing', 'testing to')
print(new_keys.get_from_key())
print(new_keys.get_to_key())