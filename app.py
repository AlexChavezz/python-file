
import RPi.GPIO as GPIO
import time


TRIG = 23


ECHO = 24

GPIO.setmode(GPIO.BCM)


GPIO.setup(TRIG, GPIO.OUT)


GPIO.setup(ECHO, GPIO.IN)

print "Medición de distancias en progreso"

try:

    while True:

        GPIO.output(TRIG, GPIO.LOW)
        print "Esperando a que el sensor se estabilice"
        time.sleep(2)


        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)


        print "Iniciando eco"
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHO) == GPIO.HIGH:
                break


        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHO) == GPIO.LOW:
                break
                
        duracion = pulso_fin - pulso_inicio

        distancia = (34300 * duracion) / 2

        print "Distancia: %.2f cm" % distancia

finally:

    GPIO.cleanup()
