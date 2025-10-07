from functions import read_csv, search_pais

df_csv = read_csv()
pais_buscado = input("Ingrese el nombre del país: ")
print(search_pais(df_csv, pais_buscado.strip()))