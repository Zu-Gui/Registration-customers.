import json
import os

clear = lambda: os.system('clear')


def create_json():
    try:
        f = open("dados.json", "x")
        f.write("{}")
    except:
        update_json()


def update_json():
    data = json.dumps(dados)
    open("dados.json", "r+").close()
    open("dados.json", "w").write(data)


try:
    with open("dados.json", "r+") as file:
        dados = json.load(file)
except:
    create_json()
    with open("dados.json", "r+") as file:
        dados = json.load(file)


def owingv(verii):
    try:
        x = float(Input(verii))
        if x != str():
            return x
    except:
        clear()
        print('=' * 30)
        print("Erro insira um número!!!")
        print('=' * 30)
        return owingv(verii)


def Input(veri):
    x = input(veri)
    if x != '':
        return x
    else:
        clear()
        print('=' * 30)
        print("Digite o campo novamente")
        print('=' * 30)
        return Input(veri)


def dump_clientes():
    for x in dados:
        print(x)


def main():
    print("Bem-Vindo ao cadastro de Clientes V.4")
    print("""            ──────▄▀▄─────▄▀▄
            ─────▄█░░▀▀▀▀▀░░█▄
            ─▄▄──█░░░░░░░░░░░█──▄▄
            █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█ \n""")

    resp = 0
    while resp != "7":
        print("[1] Adicionar cliente")
        print("[2] Consultar perfil")
        print("[3] Deletar")
        print("[4] Devedores")
        print("[5] Pagamento")
        print("[6] Clientes")
        print("[7] Sair")
        create_json()

        resp = input("Digite a opção: ")

        if resp == "1":
            clear()
            register()
        elif resp == '2':
            clear()
            query()
        elif resp == '3':
            clear()
            delete()
        elif resp == '4':
            clear()
            general_consultation()
        elif resp == '5':
            clear()
            pagament()
        elif resp == '6':
            clear()
            print("=" * 10)
            dump_clientes()
            print("=" * 10)
        elif resp == '7':
            clear()
            print("Programa finalizado")


def register():
    name = Input("Digite o nome do cliente: ")
    end = Input("Digite o endereço: ")
    fone = owingv("Digite seu telefone: ")
    pet = Input("Digite o nome do pet: ")
    owing = owingv("Digite o valor que a pessoa está devendo R$:")
    dados[name] = {"rua": end, "tel": fone, "pet": pet, "deve": owing}


def query():
    key = Input("Digite o nome para consulta: ")
    person = dados[key]
    if person:

        print(
            f"Você acessou as informações do cliente {key}\n",
            f"O endereço cliente é: {person['rua']}\n",
            f"O telefone cliente é: {person['tel']}\n",
            f"O nome do pet do cliente é: {person['pet']}\n",
            f"A pessoa esta devendo: {person['deve']},\n",
        )


def delete():
    dados.pop(input("Digite o nome de usuario para deletar: "))


def general_consultation():
    for (x, y) in dados.items():
        if y["deve"] > 0:
            print(f"A o cliente {x} está devendo R${y['deve']}")


def pagament():
    ansewer_pagament = Input(
        "Você quer adicionar divida digite [S] ou remover [R] ? ").upper()
    if ansewer_pagament == 'S':
        key_pagament = Input("Digite o nome da pessoa: ")
        for (x, y) in dados.items():
            if key_pagament in x:
                pagament_add = owingv(
                    "Digite o quanto quer adiconar de divida: ")
                result = y["deve"] = y["deve"] + pagament_add
                print(
                    f"O cliente {x} teve uma divida adicionada de {pagament_add} e a divida inteira ficou {result}"
                )
            else:
                print("Usuario não encontado!")
                break
    elif ansewer_pagament == 'R':
        for (x, y) in dados.items():
            key_pagament = Input("Digite o nome da pessoa: ")
            if key_pagament in x:
                pagament_remove = owingv(
                    "Digite o quanto quer adiconar de divida: ")
                result = y["deve"] = y["deve"] - pagament_remove
                print(
                    f"O cliente {x} teve uma divida adicionada de {pagament_remove} e a divida inteira ficou {result}"
                )
            else:
                print("Usuario não encontado!")
                break


main()
