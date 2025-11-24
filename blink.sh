#!/bin/bash  

#primeira linha inicializa interpretaçao em bash
echo 18 > /sys/class/gpio/export  # inicializa a  pinagem do gpio 18
echo out > /sys/class/gpio/gpio18/direction # seta o direcionamento da gpio 18 como saída

while [ 1 ] # loop infinito

 do
   echo 1 > /sys/class/gpio/gpio18/value # envia valor 1 (alto) para gpio 18
   sleep 0.2s # aguarda 0,2 segundos
   echo 0 > /sys/class/gpio/gpio18/value # envia valor 0 (baixo) para gpio 18
   sleep 0.2s # aguarda 0,2 segundos
 done #encerra loop

