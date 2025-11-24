# SEL0337-2025
Primeiro, vamos compreender o systemd. Ele é uma ferramenta que que implementa o estágio "Init System" do boot de inicialização do
sistema.
Ele constitui um conjunto de programas e bibliotecas responsáveis pela sequência correta de inicialização e desligamento do S.O.

Para essa prática, quer-se criar programas de uso de gpio simples e executá-los logo durante a inicialização do sistema (não 
dependendo de acessar o terminal e ativá-los manualmente). Para realizar a prática, primeiro foi redigido o programa "blink.sh". Esse
programa foi redigido em código bash para fins de aprendizado (para tal é preciso inserir uma primeira linha !/bin/bash para 
interpretação de código na linguagem bash). O códgigo "blink.sh" cria um loop infinito para ligar e desligar o led na gpio 18 com 
intervalos de tempo.

Para executar o programa durante a inicialização, é preciso conceder-lhe permissão para tal. Para isso, utiliza-se o comando "chmod"
resonsável por alterar permissões (utilizando "+" adiciona-se a permissão para o "blink.sh").

Para adicionar o programa ao conjunto de programas de inicialização, é preciso criar um novo arquivo do tipo "service", a fim de 
colocá-lo à disposição do systemd. Para isso foi criado o arquivo "Blink.service".
