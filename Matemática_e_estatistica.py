import pandas as pd
import numpy as np

#defininfo data frame com os dados de altura
altura_1 = pd.DataFrame(np.array([1.53, 1.54, 1.54, 1.54, 1.54, 1.56, 1.59, 1.60, 1.61, 1.62, 1.64, 1.64, 1.64, 1.65, 1.65, 1.65, 1.66, 1.66, 1.66, 1.67, 1.68, 1.68, 1.69, 1.71, 1.71, 1.72, 1.73, 1.73, 1.74, 1.75, 1.76, 1.76, 1.81, 1.81]), columns=['Altura'])
altura_2 = pd.DataFrame(np.array([1.40, 1.54, 1.54, 1.54, 1.54, 1.56, 1.59, 1.60, 1.61, 1.62, 1.64, 1.64, 1.64, 1.65, 1.65, 1.65, 1.66, 1.66, 1.66, 1.67, 1.68, 1.68, 1.69, 1.71, 1.71, 1.72, 1.73, 1.73, 1.74, 1.75, 1.76, 1.76, 1.81, 1.81]), columns=['Altura'])
media = altura_1.mean()

altura_1.mean()/altura_2.mean()-1



print(media)

pesos_1 = pd.DataFrame(np.array([73, 75, 90, 63, 82, 53, 64, 80, 95, 50, 48, 85, 64, 50, 84, 67, 80, 73, 75, 63, 83, 54, 79, 55, 46, 68, 83]), columns=['Peso'])
media_peso = pesos_1.mean()

print(media_peso)

pesos_1.mean()

