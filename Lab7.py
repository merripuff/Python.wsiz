import pandas as pd
data = {'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'nazwisko': ['Nowak', 'Kowalski', 'Wiśniewska', 'Jankowski'],
        'nr_albumu': [70593, 70429, 70237, 70594],
        'ocena_z_kolokwium': [4.5, 5.0, 3.5, 4.0]}
data1 = {'nr_albumu': [70593, 70429, 70237, 70594],
        'ocena_z_kolokwium_popr': [4, 5, 4.5, 3.5]}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)

# a. Wybierz studentów, którzy mają ocenę większą niż 4
oceny_wieksze_niz_4 = df[df['ocena_z_kolokwium'] > 4]

# b. Posortuj studentów według wieku (ocen)
posortowani_studenci = df.sort_values(by='ocena_z_kolokwium')

srednia_ocena_w_grupach = df.groupby('ocena_z_kolokwium')['ocena_z_kolokwium'].mean()

merged_df = pd.merge(df, df1, on='nr_albumu', how='left')

print(df)

print("\nStudenci z oceną większą niż 4:")
print(oceny_wieksze_niz_4)

print("\nStudenci posortowani według ocen:")
print(posortowani_studenci)

print("\nŚrednia ocena w każdej grupie:")
print(srednia_ocena_w_grupach)

print("\nPołączona ramka danych:")
print(merged_df)
