import pandas as pd

df = pd.read_csv("cursos-prouni.csv")
print(df.head())

for i, v in enumerate(df.columns):
    print(i, v)

print(df[df.nome == "Administração"].describe())