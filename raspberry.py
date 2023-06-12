#Importando a biblioteca
import RPi.GPIO as gpio
import time
#configurando a numeração
gpio.setmode(gpio.BOARD)
#escolhendo os botoes para entrada
gpio.setup(3, gpio.IN,pull_up_down=gpio.PUD_DOWN)
gpio.setup(5, gpio.IN,pull_up_down=gpio.PUD_DOWN)
#escolhendo os pinos dos leds para saída
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)  
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(22, gpio.OUT)

           
#atribuindo os valores BOARD para cada led
led1 = 11
led2 = 12
led3 = 13
led4 = 15
led5 = 16
led6 = 18
led7 = 19
led8 = 21
led9 = 22

           
def high(led):
  gpio.setup(led,gpio.OUT)
  gpio.output(led,gpio.HIGH)
    
def low(led):
  gpio.setup(led,gpio.OUT)
  gpio.output(led,gpio.LOW)
  
  #COMBINAÇÃO 1

def seq3():
  high(led1)
  time.sleep(2)
  low(led1)
  high(led2)
  high(led4)
  time.sleep(2)
  low(led2)
  low(led4)
  high(led3)
  high(led5)
  high(led7)
  time.sleep(2)
  high(led6)
  high(led8)
  low(led3)
  low(led5)
  low(led7)         
  time.sleep(2)
  low(led6)
  low(led8)
  high(led9)
  time.sleep(2)
  low(led9)
  time.sleep(2)
    
def seq7():
  high(led9)
  time.sleep(1)
  high(led9)
  high(led8)
  high(led6)
  time.sleep(1)
  high(led9)
  high(led8)
  high(led6)
  high(led7)
  high(led5)
  high(led3)
  time.sleep(1)
  high(led9)
  high(led8)
  high(led6)
  high(led7)
  high(led5)
  high(led3)
  high(led4)
  high(led2)
  time.sleep(1)
  high(led9)
  high(led8)
  high(led6)
  high(led7)
  high(led5)
  high(led3)
  high(led4)
  high(led2)
  high(led1)
  time.sleep(1)
  low(led9)
  low(led8)
  low(led6)
  low(led7)
  low(led5)
  low(led3)
  low(led4)
  low(led2)
  low(led1)
  time.sleep(1)

def seq11():
  high(led1)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led4)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led7)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led7)
  high(led6)
  high(led8)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led7)
  high(led6)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led9)
  low(led8)
  low(led6)
  low(led7)
  low(led5)
  low(led3)
  low(led4)
  low(led2)
  low(led1)
  time.sleep(1)
  
def seq15():
  high(led2)
  high(led3)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led7)
  high(led8)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  
def seq19():
  high(led5)
  time.sleep(1)
  high(led1)
  high(led3)
  high(led5)
  high(led7)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  low(led3)
  high(led4)
  high(led5)
  high(led6)
  low(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  high(led3)
  low(led4)
  high(led5)
  low(led6)
  high(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  high(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)

def seq23():
  high(led3)
  high(led5)
  high(led7)
  time.sleep(1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  low(led3)
  high(led4)
  low(led5)
  high(led6)
  low(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  

  #COMBINACAO2
def seq2():
  high(led9)
  time.sleep(2)
  low(led9)
  high(led8)
  high(led6)
  time.sleep(2)
  low(led9)
  low(led8)
  low(led6)
  high(led7)
  high(led5)
  high(led3)
  time.sleep(2)
  low(led9)
  low(led8)
  low(led6)
  low(led7)
  low(led5)
  low(led3)
  high(led2)
  high(led4)
  time.sleep(2)
  low(led9)
  low(led8)
  low(led6)
  low(led7)
  low(led5)
  low(led3)
  low(led2)
  low(led4)
  high(led1)
  time.sleep(2)
  low(led9)
  low(led8)
  low(led6)
  low(led7)
  low(led5)
  low(led3)
  low(led2)
  low(led4)
  low(led1)
  time.sleep(2)
  
def seq6():
  high(led1)
  high(led3)
  high(led7)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  low(led3)
  high(led4)
  low(led5)
  high(led6)
  low(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  high(led3)
  low(led4)
  high(led5)
  low(led6)
  high(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  low(led3)
  high(led4)
  low(led5)
  high(led6)
  low(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  high(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  
def seq10():
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  low(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  low(led3)
  high(led4)
  high(led5)
  low(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  high(led4)
  low(led5)
  low(led6)
  high(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  high(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)


def seq14():
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  low(led7)
  high(led8)
  high(led9)
  
  time.sleep(1)
  
  high(led1)
  high(led2)
  high(led3)
  low(led4)
  high(led5)
  high(led6)
  low(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  high(led3)
  low(led4)
  low(led5)
  high(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  high(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)

def seq18():
  high(led1)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led4)
  high(led6)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  high(led3)
  low(led4)
  high(led5)
  low(led6)
  high(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)


def seq22():
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  low(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  high(led3)
  low(led4)
  low(led5)
  low(led6)
  high(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  low(led3)
  high(led4)
  low(led5)
  high(led6)
  low(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  high(led3)
  low(led4)
  low(led5)
  low(led6)
  high(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  low(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)

  #COMBINACAO3

def seq4():
  high(led7)
  time.sleep(2)
  low(led7)
  high(led8)
  high(led4)
  time.sleep(2)
  high(led1)
  high(led5)
  high(led9)
  low(led8)
  low(led4)
  time.sleep(2)
  high(led2)
  high(led6)
  low(led1)
  low(led5)
  low(led9)
  time.sleep(2)
  low(led2)
  low(led6)
  high(led3)
  time.sleep(2)
  low(led3)
  time.sleep(2)
  
def seq8():
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  low(led6)
  high(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  low(led3)
  high(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)

def seq12():
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  high(led3)
  low(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  high(led6)
  low(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)

def seq20():
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  low(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  low(led3)
  high(led4)
  low(led5)
  high(led6)
  low(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  low(led2)
  high(led3)
  low(led4)
  low(led5)
  low(led6)
  high(led7)
  low(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  low(led3)
  high(led4)
  low(led5)
  high(led6)
  low(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  low(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)

def seq24():
  high(led1)
  high(led5)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led4)
  high(led5)
  high(led6)
  high(led8)
  high(led9)
  time.sleep(1)
  high(led1)
  high(led2)
  high(led3)
  high(led4)
  high(led5)
  high(led6)
  high(led7)
  high(led8)
  high(led9)
  time.sleep(1)
  low(led1)
  high(led2)
  high(led3)
  high(led4)
  low(led5)
  high(led6)
  high(led7)
  high(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  high(led3)
  low(led4)
  low(led5)
  low(led6)
  high(led7)
  low(led8)
  low(led9)
  time.sleep(1)
  low(led1)
  low(led2)
  low(led3)
  low(led4)
  low(led5)
  low(led6)
  low(led7)
  low(led8)
  low(led9)
  time.sleep(1)

while True:
  #CONDICIONAL DA COMBINAÇÃO 1
  if gpio.input(3) == gpio.HIGH and gpio.input(5) == gpio.LOW:
    seq3();seq7();seq11();seq15;seq19();seq23()
    
  #CONDICIONAL DA COMBINAÇÃO 2
  if gpio.input(3) == gpio.LOW and gpio.input(5) == gpio.HIGH:
    seq2();seq6();seq10();seq14();seq18();seq22()
    
    #CONDICIONAL DA COMBINAÇÃO 3
  if gpio.input(3) == gpio.HIGH and gpio.input(5) == gpio.HIGH:
    seq4();seq8();seq12();seq20();seq24()
