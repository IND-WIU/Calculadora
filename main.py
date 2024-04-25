def add(x, y): #Função de Adição
  return x + y 

def sub(x, y): #Função de Subtração
  return x - y

def mult(x, y): #Funcão de Multiplicação
  return x * y 

def div(x, y): #Função de Divisão 
  return x / y 

print("Selecione uma operação.")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
  escolha  = input("Escolha um número (1/2/3/4): ")
  if escolha in ("1" , "2" , "3" , "4"):
    num1 = float(input("Digite outro numero: "))
    num2 = float(input("Digite outro numero: ")) 
  
  if escolha == '1': 
   print(num1, "+", num2, "=", add(num1, num2 ))
    
  elif escolha == '2':
    print(num1,"-", num2, "=", sub(num1, num2 ))

  elif escolha == '3':
    print(num1, "*", num2, "=", mult(num1, num2 ))

  elif escolha == '4':
    print(num1, "/", num2, "=", div(num1, num2))

  else:
    print("Numero invalido!")
      


