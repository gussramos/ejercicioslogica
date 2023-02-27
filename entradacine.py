print('ENTRADA CINE')
print('VALOR MUJERES Y NIÑOS $8.000')
print('VALOR HOMBRES  $15.000')
edad = int(input('DIGITE SU EDAD: '))
genero = input('DIGITE GENERO F/M: ')
if edad < 18 or genero == 'F':
    valor = 8000
else:
    valor = 15000
print(f'VALOR A PAGAR: {valor}')
