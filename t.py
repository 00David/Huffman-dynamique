import string

lettres = string.ascii_letters + "éèêëàâôùûîïçÉÈÊËÀÂÔÙÛÎÏÇ"
chiffres = string.digits
ponctuation = string.punctuation
caracteres = list(lettres + chiffres + ponctuation)

print(len(caracteres))
caracteres.extend(['\n', '\r', '\t', ' '])
print(len(caracteres))
print(caracteres)