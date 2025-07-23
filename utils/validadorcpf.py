def valida_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    cpf_base = cpf[:9]

    soma = sum(int(cpf_base[i]) * (10 - i) for i in range(9))
    resto_1 = soma % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

    cpf_digito_1 = cpf_base + str(digito_1)

    soma = sum(int(cpf_digito_1[i]) * (11 - i) for i in range(10))
    resto_2 = soma % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2

    return cpf == cpf_digito_1 + str(digito_2)
