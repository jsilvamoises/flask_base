from werkzeug.security import generate_password_hash,check_password_hash

def encode_password(password):
    hash = generate_password_hash(password)
    return hash

def check_is_valid_password(password,encoded_password):
    is_valid = check_password_hash(encode_password,password)
    return is_valid

h = encode_password('jsilva.moises')
print(check_is_valid_password('jsilva.moises',h))