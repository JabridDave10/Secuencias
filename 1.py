#1. Tabla de verdad 
from machine import Pin
from utime import sleep

la = Pin(23, Pin.IN, Pin.PULL_UP)
lb = Pin(1, Pin.IN, Pin.PULL_UP)
lc = Pin(22, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    a=la.value()
    b=lb.value()
    c=lc.value()
    
    total = ((a * c) + ((not b) * (c)) + ((not a) * (b) * (not c)))
    led.value(total)
    

#2 Motor
from machine import Pin
from utime import sleep

la = Pin(23, Pin.IN, Pin.PULL_UP)
lb = Pin(1, Pin.IN, Pin.PULL_UP)
lc = Pin(22, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    a=la.value()
    b=lb.value()
    c=lc.value()
    
    total = (c *(not a) + ((not c) * (b)) + ((a) * (not b)))
    motor = (not b) * (not c) + (not a)* (not c) +(not a)* (not b)
    
    ## motor.value(motor)
    led.value(total)


#3 Seguridad

from machine import Pin
from utime import sleep

la = Pin(23, Pin.IN, Pin.PULL_UP)
lb = Pin(1, Pin.IN, Pin.PULL_UP)
lc = Pin(22, Pin.IN, Pin.PULL_UP)
ld =Pin(3,Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    a=la.value()
    b=lb.value()
    c=lc.value()
    d =ld.value()
    
    total = (not c) * (not d) + (not a) * (not b)
    led.value(total)
        

#4. Carro
from machine import Pin
from time import sleep

interruptor_pins = [Pin(23, Pin.IN, Pin.PULL_UP), Pin(22, Pin.IN, Pin.PULL_UP), Pin(21, Pin.IN, Pin.PULL_UP), Pin(3, Pin.IN, Pin.PULL_UP), Pin(19, Pin.IN, Pin.PULL_UP)]
led_pin = Pin(1, Pin.OUT)

estado_anterior = [interruptor.value() for interruptor in interruptor_pins]

while True: 
    valores = [interruptor.value() for interruptor in interruptor_pins]

    for i in range(len(valores)):
        if valores[i] != estado_anterior[i]:
            
            if sum(valores) == 0:
                led_pin.off()
            else:
                led_pin.on()

            if valores[i] == 1:
                print("El interruptor", i+1, "está abierto")
            else:
                print("El interruptor", i+1, "está cerrado")
            estado_anterior[i] = valores[i]
    sleep(0.1)