import pandas as pd

def validar_dados():
    try:
        df = pd.read_excel("C:/DevC/registroEmpregados.xlsx")

        if 'Matrícula' in df.columns:
            for index, row in df.iterrows():
                matricula = row['Matrícula']
                nome = row['Nome do empregado']
                sexo = row['Sexo']
                salario_hora = row['Salário Hora']
                horas_trabalhadas = row['Horas Trabalhadas']

                # Validação dos dados
                if not isinstance(matricula, (int, float)):
                    print(f"Erro na linha {index}: Matrícula deve ser numérica.")
                    continue  # Pular para a próxima linha
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

                # Calcular o salário total
                salario_total = calcular_salario(nome, salario_hora, horas_trabalhadas)
                # Calcular o desconto
                desconto = calcular_desconto(salario_total)
                # Calcular o salário líquido
                salario_liquido = calcular_salario_liquido(salario_total, desconto)
                print(f"Salário líquido de {nome}: R$ {salario_liquido:.2f}")

        else:
            print("A coluna 'Matrícula' não foi encontrada no arquivo.")

    except FileNotFoundError:
        print("Arquivo não encontrado")

def calcular_salario(nome, salario_hora, horas_trabalhadas):
    salario_total = salario_hora * horas_trabalhadas
    print(f"Salário total de {nome}: R$ {salario_total:.2f}")
    return salario_total  # Retorne o salário total

def calcular_desconto(salario_total):
    desconto = salario_total * 0.10
    print(f"Desconto de 10%: R$ {desconto:.2f}")
    return desconto  # Retorne o desconto

def calcular_salario_liquido(salario_total, desconto):
    return salario_total - desconto  # Salário líquido é o total menos o desconto

validar_dados()


