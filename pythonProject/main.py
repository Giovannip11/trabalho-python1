import pandas as pd

def validar_dados():
    
    print("Escolha a opção de resultado que deseja:")
    print("1 - Exibir dados de cada empregado (Matrícula, Nome, Salário Bruto, Descontos, Salário Líquido)")
    print("2 - Exibir apenas o Total dos Salários Brutos")
    opcao = input("Digite 1 ou 2: ")

    
    if opcao not in ["1", "2"]:
        print("Opção inválida! Tente novamente.")
        return

    salarios_totais = []  

    try:
       
        df = pd.read_excel("C:\\Users\\Usuário\\Desktop\\trabalho-python1-main\\registroEmpregados.xlsx")

        
        if 'Matrícula' in df.columns:
            for index, row in df.iterrows():
                matricula = row['Matrícula']
                nome = row['Nome do empregado']
                sexo = row['Sexo']
                salario_hora = row['Salário Hora']
                horas_trabalhadas = row['Horas Trabalhadas']

                
                if not isinstance(matricula, (int, float)):
                    print(f"Erro na linha {index}: Matrícula deve ser numérica.")
                    continue  
                if not nome.replace(" ", "").isalpha():
                    print(f"Erro na linha {index}: Nome deve conter apenas caracteres alfabéticos.")
                    continue
                if sexo not in ['M', 'F']:
                    print(f"Erro na linha {index}: Sexo deve ser 'M' ou 'F'.")
                    continue
                if not isinstance(salario_hora, (int, float)):
                    print(f"Erro na linha {index}: Salário Hora deve ser um valor numérico.")
                    continue
                if not isinstance(horas_trabalhadas, (int, float)):
                    print(f"Erro na linha {index}: Horas Trabalhadas deve ser um valor numérico.")
                    continue

               
                salario_total = calcular_salario(nome, salario_hora, horas_trabalhadas)
                salarios_totais.append(salario_total)  
                desconto = calcular_desconto(salario_total)
                salario_liquido = calcular_salario_liquido(nome, salario_total, desconto)

                
                if opcao == "1":
                    print("\n--- Dados do Empregado ---")
                    print(f"Matrícula: {matricula}")
                    print(f"Nome: {nome}")
                    print(f"Salário Bruto: R$ {salario_total:.2f}")
                    print(f"Desconto: R$ {desconto:.2f}")
                    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
                    print("-------------------------")

            
            total_bruto = total_salario_bruto(salarios_totais)
            if opcao == "2":
                print(f"\nTotal dos salários brutos: R$ {total_bruto:.2f}")

        else:
            print("A coluna 'Matrícula' não foi encontrada no arquivo.")

    except FileNotFoundError:
        print("Arquivo não encontrado")

def calcular_salario(nome, salario_hora, horas_trabalhadas):
    salario_total = salario_hora * horas_trabalhadas
    return salario_total  

def calcular_desconto(salario_total):
    desconto = salario_total * 0.10
    return desconto 

def calcular_salario_liquido(nome, salario_total, desconto):
    salario_liquido = salario_total - desconto 
    return salario_liquido

def total_salario_bruto(lista_salarios):
    total_salario = sum(lista_salarios)
    return total_salario


validar_dados()
