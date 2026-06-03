#pip install dvc
import pandas as pd;


dAta = {
    "name":["dushyant", "harsh", "chiatanya"],
    "age":[22, 24, 23]
}

df = pd.DataFrame(dAta)

path = "data/some.csv"
df.to_csv(path, index=False)
print("data saved to csv file")
