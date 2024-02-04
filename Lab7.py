import pandas as pd
data = {'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'nr_albumu': [70593, 70429, 70237, 70594],
        'Ocena_z_kolokwium': [4.5, 5.0, 3.5, 4.0]}
df = pd.DataFrame(data)
print(df)
