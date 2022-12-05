
salario = float(input('Digite o valor so seu salario bruto: R$ '))
dependentes = str(input('Você possui dependentes? (S/N)')).upper().strip()[0]

if dependentes == "S":
    quantidadeDependentes = int(input('Digite a quantidade de dependentes que você tem: '))
    deducaoDependente = (189.59 * 12) * quantidadeDependentes
    print(f'Você poderá deduzir da sua base de calculo: R$ {deducaoDependente :.2f}')
else:
    deducaoDependente = 0
    print('Você não tem deduções a serem feita na sua Base de Calculo de IR')

if salario <= 1903.98:
    print('Você está ISENTO do IMPOSTO RENDA!')

elif 1903.98 < salario <= 2826.65:
    aliquota = 7.5 / 100
    tributacao = 1 - 0.075
    baseCalculo = (salario * 12) - deducaoDependente
    imposto = baseCalculo * aliquota

elif 2826.65 < salario <= 3751.06:
    aliquota = 15 / 100
    tributacao = 1 - 0.15
    baseCalculo = (salario * 12) - deducaoDependente
    imposto = baseCalculo * aliquota

elif 3751.06 < salario <= 4664.68:
    aliquota = 22.5 / 100
    tributacao = 1 - 0.225
    baseCalculo = (salario * 12) - deducaoDependente
    imposto = baseCalculo * aliquota

else:
    aliquota = 27.5 / 100
    tributacao = 1 - 0.275
    baseCalculo = (salario * 12) - deducaoDependente
    imposto = baseCalculo * aliquota
