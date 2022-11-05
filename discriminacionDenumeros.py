def discriminationNumber(num, parInp):
    if num % 2 == 0:
        return {
            'parNum': [
                *parInp['parNum'],
                num
            ],
            'inpNum': parInp['inpNum']
        }

    return {
        'parNum': parInp['parNum'],
        'inpNum': [
            *parInp['inpNum'],
            num
        ]
    }

def main():
    cant = int(input("Ingrese un numero a clasificar: "))
    parInp = {
        'parNum': [],
        'inpNum': []
    }
    for i in range(cant):
        num = int(input("Ingrese un numero: "))
        parInp =  discriminationNumber(num, parInp);
        i += 1

    print("Numeros pares: ", parInp['parNum']);
    print("Numeros impares: ", parInp['inpNum']);

main();