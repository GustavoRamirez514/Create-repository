import pandas as pd

def analisis_covid_ciclo_sexo(ruta_archivo: str) -> dict:
    
    por_partes = ruta_archivo.split(".")

    if  por_partes[-1].lower() != "csv": 

        return "Formato de archivo no válido"

    
    try:
            
        dataF = pd.read_csv(ruta_archivo)

        dataF_analisis = pd.DataFrame()

        dataF_analisis["Sexo"] = dataF["Sexo"].apply(str.upper)

        def ciclo_vital(edad):
            if edad <= 5:
                return "Primera infancia"
            elif edad <= 11:
                return "Infancia"
            elif edad <= 18:
                return "Adolescencia"
            elif edad <= 26:
                return "Juventud"
            elif edad <= 59:
                return "Adultez"
            else:
                return "Persona Mayor"

        dataF_analisis["Ciclo"] = dataF["Edad"].apply(ciclo_vital)

        dataF_grupo = dataF_analisis.groupby(["Ciclo", "Sexo"]).size()
        

        return dataF_grupo.unstack().to_dict()

    except:
            return "Error procesando el archivo"

print (analisis_covid_ciclo_sexo("archivo.txt"))
print (analisis_covid_ciclo_sexo("archivo.csv"))
print (analisis_covid_ciclo_sexo("https://raw.githubusercontent.com/cesardiaz-utp/MisionTIC2022-Ciclo1-FundamentosDeProgramacion/main/clase16/Canfancia sos_positivos_de_COVID19_en_ColombiaDiezMil.csv"))