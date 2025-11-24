import RPi.GPIO as GPIO # importa biblioteca RPI GPIO
from time import sleep # importa biblioteca de tempo

GPIO.setmode(GPIO.BCM) # seta  configuração para numeração padrão das GPIO
GPIO.setwarnings(False) #desabilita avisos no terminal

pinLED = 18 # seta o led na gpio 18

GPIO.setup(pinLED, GPIO.OUT) # seta o pino 18 como gpio de saída
pwm = GPIO.PWM(pinLED, 100) #configura o pwm da gpio
pwm.start(0) #inicia a gpio com pwm em 0%

while True: 
 for i in range(0, 100, 1): #cria laço de incrementação de pwm
   pwm.start(i) #atualiza o valor de pwm
   sleep(0.5) #aguarda um tempo
