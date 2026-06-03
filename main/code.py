#pip install dvc
import pandas as pd;


dAta = {
    "name":["dushyant", "harsh", "chiatanya"],
    "age":[22, 24, 23]
}


df = pd.DataFrame(dAta)
df.loc[len(df)]=["satyarth", 21]

path = "data/some.csv"
df.to_csv(path, index=False)
print("data changed at csv file")
