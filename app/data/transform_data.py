from app.database.mongo import db
import matplotlib.pyplot as plt


class TransformData:
    def __init__(self) -> None:
        self.collections = db.get_collection()

    def get_cities_data(self):
        values = []
        for collection in self.collections:
            city = db.find_all(collection)
            city_values = []
            for i in city:
                c = float((i['data']['3']).replace('.', '').replace(',', '.'))
                city_values.append(c)
            values.append({
                'city': i['city'],
                'total': round(sum(city_values), 2)
            })

        sorted_values = sorted(values, key=lambda i: i['total'], reverse=True)

        return sorted_values

    def view_data(self, qtd):
        values = self.get_cities_data()

        cities = []
        total = []

        for value in values:
            cities.append(value['city'])
            total.append(value['total'])

        din = total[0:qtd]

        din = [f'R${i:_.2f}'.replace('.', ',').replace('_', '.') for i in din]

        din.reverse()

        fig = plt.figure(figsize=(28, 25), dpi=180)

        y = cities[0:qtd]
        x = total[0:qtd]

        y.reverse()
        x.reverse()

        fig, ax = plt.subplots()
        fig.set_figheight(10)
        fig.set_figwidth(12)

        plt.barh(y, x)
        plt.title('Custo com Eletricidade - Cidades/Ceará (Top {})'.format(qtd))

        ax.xaxis.grid(True)
        ax2 = ax.twinx()

        ax2.set_ylabel("Prefeituras", rotation=270, labelpad=25)

        ax.set_xlabel('R$ - Milhões')

        for i, v in zip(range(len(din)), x):
            ax.text(v + 2, i, din[i], color='blue', fontweight='bold')

        for tick in ax.get_yticklabels():
            tick.set_rotation(70)

        plt.savefig('cities.png')
