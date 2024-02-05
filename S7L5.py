import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 

#importo il dataframe da analizzare
file = "dataset_climatico.csv"
data_frame = pd.read_csv(file)
print(data_frame)

#pulisco il dataset da eventuali valori NaN
data_frame.dropna(inplace=True)

#aggiungo al dataframe la colonna "temperatura_media_NOR"
#che contiene la versione normalizzata con punti Z della colonna già esistente
data_frame["temperatura_media_NOR"] = (data_frame["temperatura_media"] - 
                                       data_frame["temperatura_media"].mean()) / data_frame["temperatura_media"].std()
#aggiungo al dataframe la colonna "precipitazioni_NOR"
#che contiene la versione normalizzata con punti Z della colonna già esistente
data_frame["precipitazioni_NOR"] = (data_frame["precipitazioni"] - 
                                    data_frame["precipitazioni"].mean()) / data_frame["precipitazioni"].std()

#aggiungo al dataframe la colonna "umidita_NOR"
#che contiene la versione normalizzata con punti Z della colonna già esistente
data_frame["umidita_NOR"] = (data_frame["umidita"] - 
                             data_frame["umidita"].mean())  / data_frame["umidita"].std()

#aggiungo al dataframe la colonna "velocita_NOR"
#che contiene la versione normalizzata con punti Z della colonna già esistente
data_frame["velocita_vento_NOR"] = (data_frame["velocita_vento"] - 
                                    data_frame["velocita_vento"].mean()) / data_frame["velocita_vento"].std()

#creo un nuovo dataframe contenente solo le colonne normalizzate del datframe vecchio
df_nor = pd.DataFrame({"temperatura_media_NOR": data_frame["temperatura_media_NOR"], "precipitazioni_NOR": data_frame["precipitazioni_NOR"],
                            "umidita_NOR": data_frame["umidita_NOR"], "velocita_vento_NOR":data_frame["velocita_vento_NOR"]})

#stampo il nuovo dataframe
print(df_nor)
#stampo le statistiche riassuntive di tutte le colonne 
print(data_frame.describe())

#istogramma delle temperature normalizzate
plt.hist(df_nor["temperatura_media_NOR"])
plt.title('Distribuzione della temperatura media normalizzata')
plt.xlabel('Temperatura media normalizzata')
plt.ylabel('Frequenza')
plt.show()

#box plot delle precipitazioni normalizzate
plt.boxplot(df_nor["precipitazioni_NOR"])
plt.title('Distribuzione delle precipitazioni normalizzate')
plt.ylabel('Precipitazioni normalizzate')
plt.show()

#istogramma dell'umidità normalizzata
plt.hist(df_nor["umidita_NOR"])
plt.title('Distribuzione dell\'umidità normalizzata')
plt.xlabel('Umidità normalizzata')
plt.ylabel('Frequenza')
plt.show()

#box plot della velocità del vento normalizzata
plt.boxplot(df_nor["velocita_vento_NOR"])
plt.title('Distribuzione della velocità del vento normalizzata')
plt.ylabel('Velocità del vento normalizzata')
plt.show()

# Calcolo la matrice delle correlazioni tra le variabili normalizzate
correlazioni_df_nor = df_nor.corr()
print(correlazioni_df_nor)