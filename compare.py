import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image, ImageDraw, ImageFont
import ast
import difflib
def text_to_matrix(text, width=128, height=128):
    # Normalisasi teks
    lines = text.strip().split('\n')
    normalized = ''.join(lines)  # Gabung semua baris
    normalized = ''.join(c for c in normalized if c.isalnum() or c.isspace())  # Hanya alfanumerik dan spasi
    normalized = normalized.lower()

    # Buat gambar kosong
    img = Image.new('L', (width, height), color=0)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 8)
    except:
        font = ImageFont.load_default()

    # Gambar teks ke gambar
    draw.text((0, 0), normalized[:512], fill=255, font=font)

    # Konversi ke array numpy
    matrix = np.array(img)
    return matrix

def compare_code_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
        text1 = f1.read()
        text2 = f2.read()

    matrix1 = text_to_matrix(text1)
    matrix2 = text_to_matrix(text2)
    # Hitung SSIM
    score, _ = ssim(matrix1, matrix2, full=True)
    return score,text1,text2


def get_ast_similarity(code1, code2):
    try:
        with open(code1, 'r', encoding='utf-8') as f1, open(code2, 'r', encoding='utf-8') as f2:
            text1 = f1.read()
            text2 = f2.read()
        tree1 = ast.dump(ast.parse(text1))
        tree2 = ast.dump(ast.parse(text2))
        return difflib.SequenceMatcher(None, tree1, tree2).ratio()
    except Exception as e:
        print(f"AST parsing error: {e}")
        return 0.0
