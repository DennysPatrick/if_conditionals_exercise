year = int(input('Digite o ano do seu nascimento: '))
age = 2022 - year
if age == 18:
    print('Está na hora de você se alistar no exercito.')
elif age > 18:
    print('Você já deve ter se alistado para o exercito.')
elif age < 18:
    print('Você ainda é muito novo para se alistar.')
