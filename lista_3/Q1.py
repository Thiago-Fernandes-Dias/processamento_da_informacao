area = float(input())
btuPerHour = ''
if area > 30.3:
    btuPerHour = 'Sem recomendacao'
elif area >= 25.3:
    btuPerHour = 'Recomendamos 21300 BTU/h'
elif area >= 20.3:
    btuPerHour = 'Recomendamos 18300 BTU/h'
elif area >= 15.3:
    btuPerHour = 'Recomendamos 15300 BTU/h'
elif area >= 10.3:
    btuPerHour = 'Recomendamos 12300 BTU/h'
else:
    btuPerHour = 'Recomendamos 9300 BTU/h'
print(f'Para area = {area} : {btuPerHour}')