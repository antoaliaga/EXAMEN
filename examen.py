#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
            'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
            }

#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
         'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
        }

#función para revisar stock disponible

def stock_marca(marca):
    total = 0;
    for codigo, datos in productos.items():
        if(datos[0].lower() == marca.lower()):
            total += stock[codigo][1];
    print(f"El stock total para '{marca}' es: {total}.");

#función para buscar por precio

def busqueda_precio(p_min, p_max):
    resultados = [];
    for codigo, datos in stock.items():
        precio = datos[0];
        if(precio >= p_min and precio <= p_max) and (stock[codigo][0] > 0):
            resultados.append(codigo + '--' + str(datos[0]));
    
    if resultados:
        resultados.sort();
        print("Productos encontrados:", resultados);
    else:
        print("No hay productos en ese rango de precio.");

#función para listar productos
def ordenar_productos():
        if(productos):
            productos_ordenados = sorted(productos);
            print(productos);
        else:
            print("No hay productos disponibles para mostrar.");

#función para menú principal
def main():
    while True:  
        print("***** PYBOOKS STORE *****");
        print("1. Stock marca.");
        print("2. Búsqueda por precio.");
        print("3. Listado de productos.");
        print("4. Salir.");

        try:
            opc = int(input("Ingrese una opción: "));
        
            if(opc == 1):
                marca = input("Ingrese marca de notebook: ");
                stock_marca(marca)
            
            elif(opc == 2):
                while True:  
                    try:
                        p_min = float(input("Ingrese precio mínimo: "));
                        p_max = float(input("Ingrese precio máximo: "));
                        busqueda_precio(p_min, p_max)
                        break;
                    except ValueError:
                        print("Debe ingresar números enteros.");

            elif(opc == 3):
                print("***** LISTADO DE NOTEBOOKS ORDENADOS *****");
                ordenar_productos();
            elif(opc == 4):
                print("Programa finalizado.");
                break;
            
            else:
                print("Debes ingresar una opción válida.");
        
        except ValueError:
            print("Error. Debe ingresar números.");

if __name__ == "__main__":
    main();