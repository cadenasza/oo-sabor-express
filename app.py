from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Leo', 0)
restaurante_praca.receber_avaliacao('Julia', 0)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()