
aliquota = ["isento",7.5, 15, 22.5, 27.5]
deducaoMensal = [0, 142.80, 345.80, 636.13, 869.36]
deducaoDependentes = 189.59
tributacaoRegressiva = [35, 30, 25, 20, 15, 10]
tributacaoProgressiva = ["isenta", 7.5, 15, 22.5, 27.5]
salario = aliquotaINSS = aliquotaTributacao = 0
aplicacaoPGBL = (salario * 12) * (12 / 100)

def descontoINSS(salario):
    if salario <= 1212.00:
        aliquotaINSS = 7.5
    elif 1212.00 < salario <= 2427.35:
        aliquotaINSS = 9
    elif 2427.36 < salario <= 3641.03:
        aliquotaINSS = 12
    elif 3641.03 < salario <= 7087.22:
        aliquotaINSS = 14
    else:
        aliquotaINSS = 0
    return aliquotaINSS

def baseTributacao(salario):
    if salario <= 1903.98:
        aliquotaTributacao = aliquota[0]
    elif 1903.98 < salario <= 2826.65:
        aliquotaTributacao = aliquota[1]
    elif 2826.65 < salario <= 3751.05:
        aliquotaTributacao = aliquota[2]
    elif 3751.05 < salario <= 4664.68:
        aliquotaTributacao = aliquota[3]
    else:
        aliquotaTributacao = aliquota[4]
    return aliquotaTributacao

print('=' * 100)
print(' ' * 45 + 'Bem vindo')
print(' ' * 48 + 'a')
print(' ' * 34 + 'Calculadora de IR e Previdência')
print('=' * 100)
salario = float(input('\nDigite o valor do seu salário mensal bruto: '))
print(f'\nCom a sua renda mensal, sua faixa de tribução é de {baseTributacao(salario)} %')
tributacaoSemDeducoes = (salario * 12) * (baseTributacao(salario) / 100)
print(f'\nSem as deduções, você terá que recolher valor de R$ {tributacaoSemDeducoes :.2f} de IR')

print('=' * 100)
dependentes = str(input('\nVocê possui dependentes? (S/N): ')).upper().strip()[0]

if dependentes == "S":
    quantidadeDependentes = int(input('\nQuantos dependentes você tem: '))
    valorDeducaoDependentes = deducaoDependentes * quantidadeDependentes
    print(f'\nPor você ter {quantidadeDependentes} dependentes, terá uma dedução de R${valorDeducaoDependentes} a ser descontado da sua base de tributação')
else:
    print('\nVocê não tem deduções a serem feita por dependentes')

print('=' * 100)

inss = str(input('\nVocê contribui com o INSS? (S/N): ')).upper().strip()[0]
if inss == "S":
    deducaoINSS = descontoINSS(salario)
    valorDescontado = salario * (deducaoINSS/100)
    print(f'\nSua aliquota de contribuição do INSS é de {deducaoINSS} %')
    print(f'\nO valor a ser descontado da sua base de calculo pela contribuição do INSS é de R$ {valorDescontado :.2f}')
else:
    print('\nVocê não tem deducão para fazer da sua base de calculo de Imposto de Renda')

print('=' * 100)

previdencia = str(input('\nVocê já contribui com Previdência Privada? (S/N): ')).upper().strip()[0]
if previdencia == "S":
    modalidadePrevidencia = int(input('\nQual a modalidade da sua Previdencia?'
                                      '\n[1] - PGBL '
                                      '\n[2] - VGBL '
                                      '\n[3] - Ambas' 
                                      '\nDigite a opção correspondente a sua modalidade de Previdencia: '))

    print('=' * 100)

    if modalidadePrevidencia == 1:
        aplicacaoPGBLCliente = float(input('\nQual o valor da aplicação anual da sua Previdência Privada PGBL: R$ '))
        percentualDaBaseDeCalculoPGBL = (aplicacaoPGBLCliente / (salario * 12)) * 100
        print(f'\nSua aplicação em Previdência Privada representa {percentualDaBaseDeCalculoPGBL :.1f}% da sua Base de Calculo de Imposto de Renda ')
        if percentualDaBaseDeCalculoPGBL > 12:
            excedentePGBL = percentualDaBaseDeCalculoPGBL - 12
            print(f'\nVocê excedeu em {excedentePGBL :.1f} %, por isso não estamos aproveitando ao máximo o beneficio da previdencia')
    elif modalidadePrevidencia == 2:
        aplicacaoVGBLCliente = float(input('\nQual o valor da aplicação anual da sua Previdencia Privada VGBL: R$ '))
        percentualDaBaseDeCalculoVGBL = (aplicacaoVGBLCliente / (salario * 12)) * 100
        print(f'\nSua aplicação em Previdência Privada VGBL representa {percentualDaBaseDeCalculoVGBL :.1f}% da sua Base de Calculo de Imposto de Renda')
        print('\nVocê não possui deduções a serem feitas na sua Base de calculo a ser tributada.')
    else:
        aplicacaoPGBLCliente = float(input('\nQual o valor da aplicação anual da sua Previdência Privada PGBL: R$ '))
        aplicacaoVGBLCliente = float(input('\nQual o valor da aplicação anual da sua Previdencia Privada VGBL: R$ '))
        percentualDaBaseDeCalculoPGBL = (aplicacaoPGBLCliente / (salario * 12)) * 100
        percentualDaBaseDeCalculoVGBL = (aplicacaoVGBLCliente / (salario * 12)) * 100
        print(f'\nSua aplicação em Previdência Privada PGBL representa {percentualDaBaseDeCalculoPGBL :.1f}% da sua Base de Calculo de Imposto de Renda')
        if percentualDaBaseDeCalculoPGBL > 12:
            excedentePGBL = percentualDaBaseDeCalculoPGBL - 12
            print(f'\nVocê excedeu em {excedentePGBL :.1f}%, por isso não estamos aproveitando ao máximo o beneficio da previdencia')
        print(f'\nSua aplicação em Previdência Privada VGBL representa {percentualDaBaseDeCalculoVGBL :.1f}% da sua Base de Calculo de Imposto de Renda')

    resgatePrevidencia = int(input('\nQuantos anos pretende deixar sua Previdencia Privada aplicada:'
                                   '\n[1] - até 2 anos;'
                                   '\n[2] - de 2 a 4 anos;'
                                   '\n[3] - de 4 a 6 anos;'
                                   '\n[4] - de 6 a 8 anos;'
                                   '\n[5] - de 8 a 10 anos;'
                                   '\n[6] - mais de 10 anos'
                                   '\nDigite a opção correspondente ao prazo de aplicação da Previdência: '))

else:
    novaPrevidencia = str(input('\nTem interesse em começar a aplicar em Previdência Privada? (S/N) ')).upper().strip()[0]
    if novaPrevidencia == "S":
        resgatePrevidencia = int(input('\nQuantos anos pretende deixar sua Previdencia Privada aplicada:'
                                   '\n[1] - até 2 anos;'
                                   '\n[2] - de 2 a 4 anos;'
                                   '\n[3] - de 4 a 6 anos;'
                                   '\n[4] - de 6 a 8 anos;'
                                   '\n[5] - de 8 a 10 anos;'
                                   '\n[6] - mais de 10 anos'
                                   '\nDigite a opção correspondente ao prazo de aplicação da Previdência: '))
        aporteNovaPrevidencia = float(input("\nQual o valor pretende aplicar por ano em sua Previdência Privada: "))

    print('\nAtualmente você não possui deduções a serem feitas na sua Base de calculo a ser tributada.')


print('=' * 100)



aplicacaoPGBL = (salario * 12) * (12 / 100)
print(f'\nPara aproveitar o máximo beneficio fiscal do PGBL, você pode fazer uma unica aplicação de até R$ {aplicacaoPGBL :.2f} ou aportes mensais de R${aplicacaoPGBL / 12 :.2f}')
baseTributacaoSemDeducoesComPGBL = (salario * 12) - aplicacaoPGBL
tributacaoSemDeducoesComPGBL = baseTributacaoSemDeducoesComPGBL * (baseTributacao(salario) / 100)
economiaPelaPrevidencia = tributacaoSemDeducoes - tributacaoSemDeducoesComPGBL
print(f'\nSe aplicarmos 12% da renda anual bruta em Previdência Privada PGBL, teremos uma economia de R$ {economiaPelaPrevidencia :.2f} na sua declaração de Imposto de renda!')