#Defino las letras que tienen un valor:
#Equipo a:
print("El equipo a son las letras w, p, b y s.")
print("El equipo b son las letras m, q, d y z")
print("El resto de letras son neutrales")
w = 4
p = 3
b = 2
s = 1
m = 4
q = 3
d = 2
z = 1
#Intro
text = input("Introduzca letras cualquiera")  
cant_w = text.count("w")
cant_p = text.count("p")
cant_b = text.count("b")
cant_s = text.count("s")
cant_m = text.count("m")
cant_q = text.count("q")
cant_d = text.count("d")
cant_z = text.count("z")
equipo_a = cant_w * w + cant_p * p + cant_b * b + cant_s * s
equipo_b = cant_m * m + cant_q * q + cant_d * d + cant_z * z
if equipo_a > equipo_b:
    print("Gana el equipo a por", equipo_a - equipo_b )
elif equipo_b > equipo_a:
    print("Gana el equipo b por", equipo_b - equipo_a )
else:
    print("Hubo un empate")
