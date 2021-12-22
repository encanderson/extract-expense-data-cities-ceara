from app.data.extract_and_save_data import ExtractData
from app.data.transform_data import TransformData


def main():
    req = input('Extrair novos dados? (S ou N) ')
    if req.lower() == 'sim':
        end = input('Digite um valor entre 3 e 185: ')

        data = ExtractData(int(end))

        data.start()

        trans_data = TransformData()

        qtd = int(input('Quatas cidades (1 a 184)? '))

        trans_data.view_data(qtd)
    else:
        trans_data = TransformData()

        qtd = int(input('Quatas cidades (1 a 184)? '))

        trans_data.view_data(qtd)
