from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None

def split_tiff(image_path, output_dir, tile_size=1024):
    # Abre a imagem
    img = Image.open(image_path)
    width, height = img.size

    # Cria diretório de saída
    os.makedirs(output_dir, exist_ok=True)

    count = 0
    # Percorre a imagem em blocos de 1024x1024
    for top in range(0, height, tile_size):
        for left in range(0, width, tile_size):
            box = (left, top, left + tile_size, top + tile_size)
            tile = img.crop(box)
            
            # Nome do arquivo de saída
            tile_filename = os.path.join(output_dir, f"tile_{count}.png")
            tile.save(tile_filename)
            count += 1

    print(f"✅ Divisão concluída! {count} imagens salvas em {output_dir}")

# Exemplo de uso
split_tiff(r"C:\Users\luisf\Documents\_TCC\validation.tif", "tiles_saida")
