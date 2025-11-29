
### IMPORTAR BIBLIOTECAS ###

import os
import sys

from tkinter import filedialog
from ultralytics import YOLO


### CODIGO ###

def modo_treinamento():
    print("Iniciando modo de treinamento...")

    model = YOLO('yolo11n')  # 'n' = nano

    model.train(
        data="C:/Users/luisf/Documents/_TCC/dataset.yaml",
        epochs=500, #EPOCAS
        batch=8, # numero de imagens por lote
        imgsz=1024, # tamanho da imagem
        device='0',  # Usar 0 para GPU ou 'cpu' para CPU
        save=True,  # Salva o modelo treinado
        save_period=10,  # Salva a cada 10 épocas  
        workers=10, # numero de threads do cpu
        project="C:/TCC/resultados", # define a pasta de resultados
        name="treino_mudas"  # Nome específico para esta execução
    )


def modo_detectar():
    print("Iniciando modo de detecção...")

    # Input para área total
    while True:
        try:
            area_total = float(input("Digite o tamanho da área em hectares (ex: 27.87): "))
            if area_total <= 0:
                print("Erro: A área deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("Erro: Digite um número válido (use ponto para decimais).")

    # Input para espaçamento
    while True:
        try:
            linha = float(input("Digite o espaçamento entre linhas (em metros): "))
            entrelinha = float(input("Digite o espaçamento entre entrelinhas (em metros): "))
            if linha <= 0 or entrelinha <= 0:
                print("Erro: Os espaçamentos devem ser maiores que zero.")
            else:
                break
        except ValueError:
            print("Erro: Digite números válidos.")

    # Cálculos
    num_mud_ideal_por_ha = 10000 / (linha * entrelinha)
    num_mud_ideal_total = num_mud_ideal_por_ha * area_total
    print(f"\nNúmero ideal de mudas: {num_mud_ideal_total:.0f} ({num_mud_ideal_por_ha:.0f}/ha)")


    # Selecionar modelo
    print("\nSelecione o arquivo do modelo (best.pt)...")
    model_path = filedialog.askopenfilename(
        title="Selecione o modelo treinado",
        filetypes=[("Arquivos de modelo", "*.pt"), ("Todos os arquivos", "*.*")]
    )
    if not model_path:
        print("Operação cancelada: nenhum modelo selecionado.")
        return

    # Selecionar imagem
    print("\nSelecione a imagem para análise...")
    img_path = filedialog.askopenfilename(
        title="Selecione a imagem para detecção",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png"), ("Todos os arquivos", "*.*")]
    )
    if not img_path:
        print("Operação cancelada: nenhuma imagem selecionada.")
        return

    try:
        # Carregar modelo e processar imagem
        model = YOLO(model_path)
        print("\nProcessando imagem...")
        results = model.predict(img_path,
                                save=True,
                                conf=0.3,
                                imgsz=1024)
        boxes = results[0].boxes #conta o numero de "boxes" detectados
        num_mudas = len(boxes) if boxes is not None else 0  # Corrigido para evitar erro quando boxes é 0

        # Resultados
        print("\n=== RESULTADOS ===")
        print(f"Área total: {area_total} hectares")
        print(f"Mudas detectadas: {num_mudas}")

        if num_mudas > 0:
            densidade = num_mudas / area_total
            sobrevivencia = min(1.0, num_mudas / num_mud_ideal_total)  # Limita a 100%
            mortalidade = (1 - sobrevivencia) * 100

            print(f"\nDensidade: {densidade:.2f} mudas/ha")
            print(f"Taxa de sobrevivência: {sobrevivencia:.1%}")
            print(f"Mortalidade estimada: {mortalidade:.1f}%")

        else:
            print("Nenhuma muda detectada na imagem.")

    except Exception as e:
        print(f"\nErro durante a detecção: {str(e)}")


def treinar_a_ia():
    print("\nAbrindo LabelImg para anotação...")
    try:
        # Tentativa universal de abrir o LabelImg
        if sys.platform == 'win32':
            os.startfile("labelImg") \
                if hasattr(os, 'startfile') \
                else os.system("labelImg")
        else:
            os.system("labelImg &")  # para rodar no Linux/Mac

        print("✓ LabelImg iniciado com sucesso")

    except Exception as e:
        print(f"Erro crítico: {str(e)}")
        print("\nSoluções alternativas:")
        print("1. Execute manualmente no terminal: labelImg")
        print("2. Instale via: pip install labelImg --upgrade")
        print("3. Use o caminho completo: C:/.../Python/Scripts/labelImg.exe")


def main():
    print("\nSistema de Análise de mortalidade de mudas florestais")
    while True:
        entrada = input("\nSelecione o modo (1-LabelImg, 2-Treinamento, 3-Detectar, 4-Sair): ").strip().lower()

        if entrada in ['1', 'labelimg']:
            treinar_a_ia()
        elif entrada in ['2', 'treinamento']:
            modo_treinamento()
        elif entrada in ['3', 'detectar']:
            modo_detectar()
        elif entrada in ['4', 'sair']:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()

