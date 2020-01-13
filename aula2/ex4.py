while True:
        try:
            salario_velho = float(input("Coloque o salario: "))
            break
        except ValueError:
            print("Não colocou um salario valido\n")


percentual = 7 / 100
imposto = salario_velho * percentual
percentual = 5 / 100
gratificacao = salario_velho * percentual
salario_novo = salario_velho + gratificacao - imposto

salario_velho = round(salario_velho)
gratificacao = round(gratificacao, 2)
imposto = round(imposto, 2)
salario_novo = round(salario_novo, 2)

print(f"O salario de R${salario_velho} teve uma gratificação de R${gratificacao} com impostos de R${imposto}\n" +
      f"Salario total de R${salario_novo}")
