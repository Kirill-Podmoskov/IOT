import matplotlib.pyplot as plt

counts = [17, 3]
plt.figure(figsize=(5, 5))
plt.pie(counts,
        colors=['c', 'gold'],
        labels=['Собаки', 'Кошки'],
        startangle=120,
        autopct='%.1f%%')

plt.title('Круговая диаграмма для собак и кошек')
plt.show()
