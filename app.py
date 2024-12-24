from modelos.restaurante import Restaurante  # Importa a classe Restaurante do módulo modelos.restaurante


# Cria um novo objeto Restaurante com o nome 'praca' e categoria 'Gourmet'
restaurante_praca = Restaurante('praca', 'Gourmet')
# Adiciona três avaliações ao restaurante
restaurante_praca.receber_avalicacao('Gui', 2)  # Avaliação do cliente Gui com nota 10
restaurante_praca.receber_avalicacao('Lais', 2)  # Avaliação do cliente Lais com nota 8
restaurante_praca.receber_avalicacao('Emy', 2)  # Avaliação do cliente Emy com nota 5


def main():
    # Função principal que lista todos os restaurantes
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    # Verifica se o script está sendo executado diretamente (e não importado como módulo)
    main()  # Chama a função principal
