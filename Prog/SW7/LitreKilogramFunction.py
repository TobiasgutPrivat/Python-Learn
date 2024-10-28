def LitreToKilogram(litres, density):
    return litres * density

litres = int(input("Litres (L): "))
density = int(input("Density (kg/L): "))

print("Kilograms (kg): ",LitreToKilogram(litres, density))