from grafico import grafico_muletillas as grafico
import os

def main():
    print("ejecutado")
    ruta_json= "resultado/repetitions.json"
    dirpath = os.path.dirname(os.path.abspath(__file__))
    grafico_usuario = grafico.Filler_Graphic()
    graf= grafico_usuario.new_graphic("786", ruta_json , dirpath)
    print("ejecutado")

if __name__ == '__main__':
    main()