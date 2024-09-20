print("Actividad 9 Clase Humano")
print("Zyanya Mireles Mat: 22308051281080")

# Zona de clases 
class Humano1080:
    #zona de atributos
    fech_nacF = ""
    padresF = ""
    generoF = ""
    color_peloF = ""

    fech_nacM = ""
    generoM = ""
    peso = 0
    estatura = 0
    color_ojos = ""

    #zona de funciones dentro de la clase 
    def dormir1080(self,n):
        print(f"\n{n} está mimida")

    def comer1080(self,n):
        print(f"{n} está comiendo")

    def leer1080(self,n):
        print(f"{n} está leyendo")
    
    def caminar1080(self,n):
        print(f"{n} está caminando")


    def escuchar_musica1080(self,m):
        print(f"\n{m} está escuchando música")

    def pintar1080(self,m):
        print(f"{m} está pintando")

    def tocar_piano1080(self,m):
        print(f"{m} está tocando el piano")

    def mensaje1080(self,m):
        print(f"{m} está mensajeando")
    
    def bailar1080(self,m):
        print(f"{m} está bailando")


#zona de creación de objetos
Zyanya = Humano1080()
El = Humano1080()
#zona de usando objetos
print("\nResultados para Zyanya")

Zyanya.fech_nacF = "14 de Abril del 2007"
Zyanya.padresF = "Agustina y Sergio"
Zyanya.generoF = "Femenino"
Zyanya.color_peloF = "Negro"

print(f"Fecha de nacimiento: {Zyanya.fech_nacF}")
print(f"Padres: {Zyanya.padresF}")
print(f"Genero: {Zyanya.generoF}")
print(f"Color de pelo: {Zyanya.color_peloF}")

Zyanya.dormir1080("Zyanya")
Zyanya.comer1080("Zyanya")
Zyanya.leer1080("Zyanya")
Zyanya.caminar1080("Zyanya")


print("\nResultados para Él")

El.fech_nacM = "22 de Marzo del 2007"
El.generoM = "Masculino"
El.peso = 70
El.estatura = 1.68
El.color_ojos = "Café"

print(f"Fecha de nacimiento: {El.fech_nacM}")
print(f"Genero: {El.generoM}")
print(f"Peso: {El.peso}")
print(f"Estatura: {El.estatura}")
print(f"Color de ojos: {El.color_ojos}")

El.escuchar_musica1080("Él")
El.pintar1080("Él")
El.tocar_piano1080("Él")
El.mensaje1080("Él")
El.bailar1080("Él")