import pandas as pd
data = {'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'nazwisko': ['Nowak', 'Kowalski', 'Wiśniewska', 'Jankowski'],
        'nr_albumu': [70593, 70429, 70237, 70594],
        'ocena_z_kolokwium': [3, 3.5, 4, 3]}
data1 = {'nr_albumu': [70593, 70429, 70237, 70594],
        'ocena_z_kolokwium_popr': [4.5, 5, 4.5, 3.5]}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)

oceny_wieksze_niz_4 = df[df['ocena_z_kolokwium'] > 4]

posortowani_studenci = df.sort_values(by='ocena_z_kolokwium')

srednia_ocena_w_grupach = df.groupby('ocena_z_kolokwium')['ocena_z_kolokwium'].mean()

merged_df = pd.merge(df, df1, on='nr_albumu', how='left')

merged_df.to_csv('merged_data.csv')

print(df)

print("\nStudenci z oceną większą niż 4:")
print(oceny_wieksze_niz_4)

print("\nStudenci posortowani według ocen:")
print(posortowani_studenci)

print("\nŚrednia ocena w każdej grupie:")
print(srednia_ocena_w_grupach)

print("\nPołączona ramka danych:")
print(merged_df)

print("\nPlik CSV został pomyślnie zapisany.")
