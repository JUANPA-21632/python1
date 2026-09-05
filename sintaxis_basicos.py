nombre = "Juan" #variable texto (string)
documento = 12345678 #variable numerica (int)
direccion = "Medellin" #variable texto (string)
tiene_deuda = True #variable booleana (bool)

#mostra el valor de la variable
print(nombre)


print ("concatenacion usando +")
print ("="* 30 )

print ("Mi nombre es: " + nombre)
print ("Mi documento es: " + str(documento))

print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))



print ("\nconcatenacion usando ,")
print ("="* 30 )

print ("Mi nombre es: ", nombre, "documento: ", documento)

print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

print(f"Mi nombre es: {nombre} y mi documento es: {documento}")

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

print(f"""
Mi nombre es: {nombre}
Mi documento es: {documento}
Mi dirección es: {direccion}
Tengo deuda: {tiene_deuda}
""")

print(f"\n Hola, {nombre}!")

print(f"Bienvenido {nombre} a Python.\n")

