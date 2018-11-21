"""
This script exports top 30 popular cities from dataset(https://gist.github.com/nalgeon/5307af065ff0e3bc97927c832fabe26b)

Author: Alik Khilazhev

"""
import pandas


df = pandas.read_csv('../dataset/cities.csv', encoding = 'utf8')

df["Население"] = df["Население"].apply(pandas.to_numeric)

df = df.sort_values(by='Население', ascending=False)[:30]

df = df[["Город", "Широта", "Долгота", "Население"]]

df.to_csv('../dataset/top30_cities.csv', encoding='utf8')