import pandas as pd
import os
def main():
      caminho_entrada = os.path.join("data", "pacientes_hospitalar.csv")
      caminho_saida = os.path.join("data", "pacientes_hospitalar_tratado.csv")

      df = pd.read_csv(caminho_entrada)
      df_tratado = df.copy()

      df_tratado['Age'] = pd.to_numeric(df_tratado['Age'], errors='coerce').astype('Int64')
      df_tratado['AdmissionDate'] = pd.to_datetime(df_tratado['AdmissionDate'], errors='coerce')
      df_tratado['DischargeDate'] = pd.to_datetime(df_tratado['DischargeDate'], errors='coerce')

      df_tratado['Gender'] = df['Gender'].fillna("Não Informado")
      df_tratado.loc[df_tratado['Gender'].isin(['Other', 'Unknown']), 'Gender'] = 'Não Informado'
      df_tratado['Gender'] = df_tratado['Gender'].replace({
            "Male": "Homem",
            "Female": "Mulher"
      })

      df_tratado['Diagnosis'] = (
            df_tratado['Diagnosis']
            .str.strip()
            .str.upper()
            .fillna('Não Informado')
      )

      mask_datas_erradas = df_tratado['DischargeDate'] < df_tratado['AdmissionDate']
      df_tratado.loc[mask_datas_erradas, ['AdmissionDate', 'DischargeDate']] = \
            df_tratado.loc[mask_datas_erradas, ['DischargeDate', 'AdmissionDate']].values
      
      df_tratado['LengthOfStay'] = (
            (df_tratado['DischargeDate'] - df_tratado['AdmissionDate']).dt.days
      )

      df_tratado['Diagnosis'] = df_tratado['Diagnosis'].fillna('Não Informado')
      map_diagnpstico = {
            "MYOCARDIAL INFARCTION": "Infarto do Miocárdio",
            "PNEUMONIA": "Pneumonia",
            "INFLUENZA": "Influenza",
            "ACUTE BRONCHITIS": "Bronquite Aguda",
            "TYPE 2 DIABETES": "Diabetes Tipo 2",
            "GASTROENTERITIS": "Gastroenterite",
            "URINARY TRACT INFECTION": "Infecção do Trato Urinário",
            "DIVERTICULITIS": "Diverticulite",
            "CHOLELITHIASIS": "Colelitíase",
            "HYPERTENSION": "Hipertensão",
            "CHRONIC KIDNEY DISEASE": "Doença Renal Crônica",
            "ATRIAL FIBRILLATION": "Fibrilação Atrial",
            "ASTHMA": "Asma",
            "OSTEOARTHRITIS": "Osteoartrite"
      }

      df_tratado['Diagnosis'] = df_tratado['Diagnosis'].replace(map_diagnpstico)

      df_tratado['Flag_DataError'] = mask_datas_erradas
      df_tratado['Flag_AgeMissing'] = df_tratado['Age'].isna()
      df_tratado['Flag_DiadnosisMissing'] = df_tratado['Diagnosis'] == 'Não Informado'



      print(df_tratado.head())
      df_tratado.to_csv(caminho_saida, 
                        index=False,
                        encoding='utf-8-sig')
      print(df_tratado['Diagnosis'].unique())
if __name__ == "__main__":
      main()