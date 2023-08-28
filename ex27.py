import random
def create_password_generator(symbols):
    def password_generator(count):
        password = []
        for i in range(count):
            password.append(random.choice(symbols))
        return ''.join(password)

    return password_generator

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))
print(alpha_password(10))

print(symbol_password(5))
print(symbol_password(10))
        