from models.cliente import Cliente
from models.conta import Conta

feliciy: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '02/09/1987')

angelina: Cliente = Cliente('Anjelina Jolie', 'angelina@gmail.com', '123.456.789-02', '02/09/1978')

# print(feliciy)
# print(angelina)

contaf: Conta = Conta(feliciy)
contaA: Conta = Conta(angelina)

print(contaf)
print(contaA)
