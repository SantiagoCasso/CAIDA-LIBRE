import math
import serial
import time

# Configura el puerto serial
puerto_serial = serial.Serial('COM3', 9600, timeout=1)

# Inicializa variables para el tiempo de inicio, fin, velocidad, distancia,gravedad,etc
tiempo_inicio = 0
tiempo_fin = 0
dis=0
velocidad=0
gravedad=9.8


# Espera a que se establezca la conexión
time.sleep(2)

while True:
    # Lee una línea desde el puerto serial
    lectura_serial = puerto_serial.readline().decode().strip()
    
    # Verifica si la lectura indica que el LED se ha encendido
    if lectura_serial == "LED Encendido":
        print("El LED se ha encendido.")
        # Registra el tiempo de inicio
        tiempo_inicio = time.time()
    # Verifica si la lectura indica que el LED se ha apagado
    elif lectura_serial == "LED Apagado":
        print("El LED se ha apagado.")
        # Registra el tiempo de fin
        tiempo_fin = time.time()
        # Calcula la diferencia de tiempo
        tiempo_transcurrido = tiempo_fin - tiempo_inicio
        print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
        break

# Cierra el puerto serial
puerto_serial.close()


#calculos
dis=(gravedad*(tiempo_transcurrido**2))/2
velocidad=math.sqrt(2*(gravedad*dis))
print("la velocidad final es: "+ str(velocidad)+" m/s"+"\nla distancia a la que fue soltado el objeto fue: "+str(dis)+" metros")





