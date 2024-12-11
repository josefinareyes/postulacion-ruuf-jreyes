def max_solar_panels(a, b, x, y):

    panels_a = (x // a) * (y // b) + ((x % a) // b) * (y // a)
    panels_b = (x // b) * (y // a) + ((x % b) // a) * (y // b)

    panels_c = (y // a) * (x // b) + ((y % a) // b) * (x // a)
    panels_d = (y // b) * (x // a) + ((y % b) // a) * (x // b)

    return max(panels_a, panels_b, panels_c, panels_d)

def main():
    a = int(input("Ingrese el ancho del panel: "))
    b = int(input("Ingrese el alto del panel: "))
    
    x = int(input("Ingrese el ancho del techo: "))
    y = int(input("Ingrese el alto del techo: "))
    
    result = max_solar_panels(a, b, x, y)
    print(f"Cantidad máxima de paneles: {result}")

if __name__ == "__main__":
    main()
