# ==========================================
# Fase 5 - Evaluación Final POA
# Problema 2: Precios de menú de restaurante
# ==========================================

def calcular_precio_final(precio_base, categoria_producto, categoria_objetivo, umbral_precio):
    """
    Módulo que calcula el precio final de un producto.
    Aplica un 15% de descuento si cumple con la categoría objetivo y supera el umbral de precio.
    """
    if categoria_producto == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        return precio_base - descuento
    else:
        return precio_base

def main():

    menu = [
        ["Hamburguesa Sencilla", "Comida Rápida", 18000],
        ["Pizza Familiar", "Comida Rápida", 45000],       
        ["Ensalada César", "Saludable", 22000],
        ["Wrap de Pollo", "Saludable", 15000],
        ["Corte Ribeye", "Carnes", 60000],
        ["Papas Fritas", "Comida Rápida", 12000]          
    ]

    categoria_promo = "Comida Rápida"
    umbral_promo = 20000

    print("=" * 45)
    print("   SISTEMA DE PRECIOS Y PROMOCIONES")
    print("=" * 45)
    print(f"Promoción: 15% de descuento en la categoría '{categoria_promo}'")
    print(f"para productos con precio base mayor a ${umbral_promo}\n")

    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        precio_final = calcular_precio_final(precio_base, categoria, categoria_promo, umbral_promo)


        print(f"Producto: {nombre} ({categoria})")
        print(f"Precio Base:  ${precio_base:,.2f}")
        print(f"Precio Final: ${precio_final:,.2f}")
        
        if precio_final < precio_base:
            print(" -> ¡Descuento del 15% aplicado!")
            
        print("-" * 45)

if __name__ == "__main__":
    main()
    
    print("\n¡Gracias por usar el sistema de precios y promociones!")