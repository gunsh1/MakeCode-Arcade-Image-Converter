from PIL import Image
import pyperclip
import colorsys
import numpy as np
from math import ceil, gcd

def simplify_size(width, height, min_size=50, max_size=80):
    factor = gcd(width, height)
    scale_factor = max(min_size / min(width, height), min(max_size / max(width, height), 1))
    simplified_width = round(width * scale_factor)
    simplified_height = round(height * scale_factor)
    return simplified_width, simplified_height

def image_to_makecode_format():
    # ユーザーに画像パスを入力させる / Ask the user to input the image path
    image_path = input("変換する画像のパスを入力してください / Enter the path of the image to convert: ").strip().strip('"')
    
    # 画像を開く / Open the image
    image = Image.open(image_path).convert('RGBA')  # RGBAに変更して透明度も考慮 / Convert to RGBA to handle transparency
    original_width, original_height = image.size

    # ユーザーにMakeCode Arcadeのピクセル数を入力させる / Ask the user to input the pixel dimensions
    user_height = int(input("MakeCode Arcadeの縦のピクセル数を入力してください (0 で自動調整) / Enter the height in pixels for MakeCode Arcade (0 for auto): ").strip())
    if user_height == 0:
        output_width, output_height = simplify_size(original_width, original_height)
    else:
        user_width = int(input("MakeCode Arcadeの横のピクセル数を入力してください / Enter the width in pixels for MakeCode Arcade: ").strip())
        output_width, output_height = user_width, user_height

    # 正確なMakeCode Arcadeのカラーパレット / Accurate MakeCode Arcade color palette
    palette = [
        (174, 174, 174), (255, 255, 255), (255, 33, 33), (255, 147, 196),
        (255, 129, 53), (255, 246, 9), (36, 156, 163), (120, 220, 82),
        (0, 63, 173), (135, 242, 255), (142, 46, 196), (164, 131, 159),
        (92, 64, 108), (229, 205, 196), (145, 70, 61), (0, 0, 0)
    ]

    # 領域の平均色を取得（透明色を考慮） / Get the average color of a region (consider transparency)
    def average_color(x_start, y_start, block_size_x, block_size_y):
        x_start, y_start = int(x_start), int(y_start)
        x_end, y_end = min(original_width, x_start + block_size_x), min(original_height, y_start + block_size_y)
        region = image.crop((x_start, y_start, x_end, y_end))
        pixels = np.array(region)
        
        # アルファ値のチェック（透明なら白にする） / Check alpha value (use white if transparent)
        if pixels.shape[-1] == 4:  # RGBAの場合 / If RGBA
            alpha = pixels[:, :, 3]
            mask = alpha > 0  # 透明でないピクセル / Non-transparent pixels
            if np.any(mask):
                rgb_values = pixels[:, :, :3][mask].mean(axis=0)  # 非透明部分の平均 / Average of non-transparent parts
            else:
                rgb_values = np.array([255, 255, 255])  # 透明なら白 / Use white if transparent
        else:
            rgb_values = pixels[:, :, :3].mean(axis=(0, 1))
        return rgb_values

    # より適切な色選択 (RGB + HSVの両方考慮) / Choose the best color (considering both RGB and HSV)
    def closest_color(avg_rgb):
        h1, s1, v1 = colorsys.rgb_to_hsv(avg_rgb[0] / 255, avg_rgb[1] / 255, avg_rgb[2] / 255)
        
        def color_distance(c):
            cr, cg, cb = c
            h2, s2, v2 = colorsys.rgb_to_hsv(cr / 255, cg / 255, cb / 255)
            rgb_dist = ((avg_rgb[0] - cr) ** 2 + (avg_rgb[1] - cg) ** 2 + (avg_rgb[2] - cb) ** 2) ** 0.5
            hsv_dist = (abs(h1 - h2) * 2) ** 2 + (abs(s1 - s2) * 1.5) ** 2 + (abs(v1 - v2) * 1) ** 2
            return rgb_dist * 0.7 + hsv_dist * 0.3  # RGBとHSVを組み合わせた評価 / Combine RGB and HSV evaluations
        
        return min(palette, key=color_distance)

    # ピクセルデータを変換（均等な座標でサンプリング） / Convert pixel data (sample at even intervals)
    pixel_data = []
    block_size_x = ceil(original_width / output_width)
    block_size_y = ceil(original_height / output_height)
    
    for y in np.arange(0, original_height, block_size_y):
        row = []
        for x in np.arange(0, original_width, block_size_x):
            avg_rgb = average_color(x, y, block_size_x, block_size_y)
            closest = closest_color(avg_rgb)
            color_index = palette.index(closest)
            row.append(hex(color_index)[2:])
        pixel_data.append(row)

    # MakeCode Arcade形式の文字列を作成 / Create MakeCode Arcade formatted string
    makecode_data = f"img`\n{chr(10).join([' '.join(row) for row in pixel_data])}\n`"

    # デバッグ用: コンソールに出力 / Output to console for debugging
    print("--- 変換結果 / Conversion Result ---")
    print(makecode_data)

    # クリップボードにコピー / Copy to clipboard
    pyperclip.copy(makecode_data)
    print("MakeCode Arcade形式のデータをクリップボードにコピーしました！ / The data in MakeCode Arcade format has been copied to the clipboard!")

# 画像パスをユーザー入力で指定 / Specify image path through user input
image_to_makecode_format()
