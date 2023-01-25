import matplotlib.pyplot as plt
import json
import os
import requests
import pandas as pd 

class Filler_Graphic:

    recomendation = """Steven D. Cohen, un experto internacionalmente conocido en 
    comunicación de liderazgo, presencia ejecutiva y oratoria persuasiva, 
    recomienda que la mejor forma de minimizar el uso de muletillas es realizar 
    una pausa de silencio. Este espacio nos permite pensar y nos hace sonar seguros 
    y en control, mientras que las muletillas en exceso distraen y le dan al público 
    una percepción de falta de conocimientos del orador.""".replace("\n","")


    def url_user(self, datos_imagenes, dirpath): #Genera el directorio del grafico para usuario
        url_path_user= dirpath + "/" + datos_imagenes['resultado_id']
        if not os.path.exists(url_path_user):
            os.makedirs(url_path_user)
            os.makedirs(url_path_user+"/muletillas")
        return url_path_user
        

    def request_server(self, archivos_imagenes, datos_imagenes, url_path_user): #Request para enviar imagen de muletillas
        url = 'https://rap.cti.espol.edu.ec/'
        datos_muletillas = url_path_user+ '/muletillas/grafico_muletillas.png'
        archivos_imagenes['img_0'] = open(datos_muletillas,'rb')
        r = requests.post(url + 'resultados/guardar_imagenes/', data=datos_imagenes,files=archivos_imagenes)
        print(r)


    def new_graphic(self, resultado_id, muletillas_json, dirpath):
        #dirpath = os.path.dirname(os.path.abspath(__file__))

        #Data para guardar y enviar el grafico
        datos_imagenes = {}
        archivos_imagenes = {}

        datos_imagenes['clave'] = 'rapIsFun'
        datos_imagenes['resultado_id'] = resultado_id
        datos_imagenes['num_images'] = 1
        datos_imagenes['img_type_0'] = 'f'
        datos_imagenes['classifier_0'] = 'filler'

        #Genera el grafico
        dictionary = json.load(open(muletillas_json, 'r'))
        xAxis = []
        yAxis = []
        for key, value in dictionary.items():
            if(value != 0):
                value = value
                xAxis.append(key)
                yAxis.append(value)


        df = pd.DataFrame(dict(filler_words=xAxis,count=yAxis))
        df_sorted = df.sort_values('count')
        fig, ax =  plt.subplots(figsize =(8, 5))       
        plt.bar('filler_words', 'count',data=df_sorted,  color='maroon', width = 0.4)
        plt.xlabel('Muletillas')
        plt.ylabel('Cantidad de muletillas detectadas en la presentación')
        #plt.show()

        user_path= self.url_user(datos_imagenes, dirpath)
        plt.savefig(user_path+'/muletillas/grafico_muletillas.png')
        #self.request_server(archivos_imagenes, datos_imagenes, user_path)
