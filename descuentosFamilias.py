def descEstrato(consumo, estrato):
    descuento = 0;

    if estrato == 1:
        descuento = consumo * 0.2
    elif estrato == 2:
        descuento = consumo * 0.15
    elif estrato == 3:
        descuento = consumo * 0.9
  
    return descuento

def descIntegrantes(consumo, cantidadDeIntegrantes):
    descuento = 0;

    if cantidadDeIntegrantes >= 5:
        descuento = consumo * 0.2
    elif cantidadDeIntegrantes >= 4:
        descuento = consumo * 0.15
    elif cantidadDeIntegrantes >= 3:
        descuento = consumo * 0.1
    
    return descuento
        

def descuentos(consumo, estrato, cantidadDeIntegrantes):
    resDescEstrato = descEstrato(consumo, estrato);
    resDescIntegrantes = descIntegrantes(consumo, cantidadDeIntegrantes);
    return resDescEstrato + resDescIntegrantes;


def main():
    CANTIDAD_FAMILIAS = int(input("Ingrese la cantidad de familias: "))
    listaFamilias = [];

    for i in range(CANTIDAD_FAMILIAS):
        print("Familia ", i+1)
        nombreDeFamilia = input("Ingrese el nombre de la familia: ")
        cantidadDeIntegrantes = int(input("Ingrese la cantidad de integrantes de la familia: "))
        estrato = int(input("Ingrese el estrato de la familia: "))
        consumoDeAgua = int(input("Ingrese el consumo de agua de la familia: "))
        consumoDeLuz = int(input("Ingrese el consumo de luz de la familia: "))
        descuentoAgua = descuentos(consumoDeAgua, estrato, cantidadDeIntegrantes);
        descuentoLuz = descuentos(consumoDeLuz, estrato, cantidadDeIntegrantes);
        

        listaFamilias.append({
            "nombreDeFamilia": nombreDeFamilia,
            "cantidadDeIntegrantes": cantidadDeIntegrantes, 
            "estrato": estrato, 
            "consumoDeAgua": {
                "consumo": consumoDeAgua,
                "descuento": descuentoAgua,
                "total": (consumoDeAgua - descuentoAgua)
            },
            "consumoDeLuz": {
                "consumo": consumoDeLuz,
                "descuento": descuentoLuz,
                "total": (consumoDeLuz - descuentoLuz)
            }

        });

    print("Familias: ", listaFamilias)   
        
        

main();
