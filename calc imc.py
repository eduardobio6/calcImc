#Calculadora de IMC

print('--------------------------------------Calculadora de imc em python--------------------------------------\n')
nome = input('Por favor digite o seu nome: ')
altura = float(input('Agora precisamos saber a sua altura:'))
peso = float(input('Agora digite o seu peso: '))
imc = peso / altura ** 2

if imc >= 18.5 and imc <= 24.9:
    print(f'Parabens {nome}, o resultado do calcula foi de: {imc:.2F} e é considerado ideal para a sua altura :D')
elif imc >= 25 and imc <= 29.9:
     print(f'{nome}, o resultado do calculo foi de: {imc:.2F} e é considerado como sobrepeso')
elif imc >= 30 and imc <= 39.9:
     print(f'{nome}, o resultado do calculo foi de: {imc:.2F} e já é considerado obsidade morbida grau I')
elif imc >= 40:
    print(f'{nome}, o resultado do calculo foi de: {imc:.2F} e já é condiderado obesidade morbida grau II')
else:
    print('RESULTADO INVALIDO!!!!')
