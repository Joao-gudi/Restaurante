from modelos.Avaliacao import Avaliacao  # Importa a classe Avaliacao do módulo modelos


class Restaurante:
    restaurantes = []  # Inicializa uma lista de classe que armazenará todos os objetos Restaurante

    def __init__(self, nome, categoria):
        # Inicializa um novo restaurante com o nome e categoria fornecidos
        self._nome = nome.title()  # Nome formatado com a primeira letra maiúscula
        self._categoria = categoria.upper()  # Categoria em maiúsculas
        self._ativo = False  # Estado inicial do restaurante é inativo
        self._avaliacao = []  # Lista de avaliações do restaurante
        Restaurante.restaurantes.append(self)  # Adiciona o restaurante à lista de classe
    

    def __str__(self):
        # Retorna uma representação em string do restaurante
        return f'{self._nome} | {self._categoria}'
    

    @classmethod
    def listar_restaurantes(cls):
        # Método de classe para listar todos os restaurantes
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')  # Imprime o cabeçalho da tabela
        for restaurante in cls.restaurantes:
            # Itera sobre todos os restaurantes na lista de classe e imprime os atributos de cada um
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    

    @property
    def ativo(self):
        # Propriedade para retornar o estado do restaurante como um ícone
        return '✅' if self._ativo else '❌'
    

    def alternar_estado(self):
        # Método para alternar o estado ativo/inativo do restaurante
        self._ativo = not self._ativo
    

    def receber_avalicacao(self, cliente, nota):
        if 0 < nota <= 5:
            
            # Método para receber uma nova avaliação e adicioná-la à lista de avaliações
            avaliacao = Avaliacao(cliente, nota)  # Cria uma nova avaliação com o cliente e a nota fornecidos
            self._avaliacao.append(avaliacao)  # Adiciona a avaliação à lista de avaliações
    

    @property
    def media_avaliacoes(self):
        # Propriedade para calcular e retornar a média das avaliações
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)  # Soma todas as notas das avaliações
        quantida_de_notas = len(self._avaliacao)  # Conta o número de avaliações
        media = round(soma_das_notas / quantida_de_notas, 1)  # Calcula a média arredondada para uma casa decimal
        return media  # Retorna a média das avaliações
