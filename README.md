### **README.md**
```md
# 🎨 MakeCode Arcade Image Converter

このプロジェクトは、画像を [MakeCode Arcade](https://arcade.makecode.com/) で使用できるピクセルアート形式に変換する Python スクリプトです。

This project is a Python script that converts images into a pixel art format compatible with [MakeCode Arcade](https://arcade.makecode.com/).
```
---

## 🛠️ 必要な環境 / Requirements
- Python 3.7 以上 / Python 3.7 or later  
- `Pillow`, `numpy`, `pyperclip` ライブラリのインストールが必要です / Requires `Pillow`, `numpy`, and `pyperclip` libraries.

### 📦 インストール方法 / Installation
以下のコマンドを実行して、必要なライブラリをインストールしてください：  
Run the following command to install the required libraries:
```bash
pip install pillow pyperclip numpy
```
---

## 🏃‍♂️ 使い方 / Usage
1. ターミナルまたはコマンドプロンプトを開き、スクリプトを実行 / Open a terminal or command prompt and run the script:
   ```bash
   python MakecodePixelConvert.py
   ```
2. **画像のパスを入力**（例: `C:\images\example.png` または `/home/user/images/example.png`）  
   **Enter the image path** (e.g., `C:\images\example.png` or `/home/user/images/example.png`)
3. **MakeCode Arcade のピクセル数を指定** / **Specify the pixel dimensions for MakeCode Arcade**:
   - 縦のピクセル数を入力（`0` で自動調整）  
     Enter the **height** in pixels (`0` for auto adjustment).
   - `0` 以外を入力した場合、次に横のピクセル数を入力  
     If you enter a non-zero value, then enter the **width** in pixels.
4. 変換結果が **クリップボードにコピーされます**  
   The conversion result will be **copied to the clipboard**.
5. **MakeCode Arcade の JavaScriptエディター または ピクセルエディターで使用可能**  
   The result can be used in the **JavaScript editor or the Pixel Editor** in [MakeCode Arcade](https://arcade.makecode.com/).

---

## 🔄 変換の仕組み / Conversion Process
- **色変換 / Color Mapping**：  
  RGB + HSV の組み合わせで、最も近い MakeCode Arcade の16色パレットを選択。  
  Uses a combination of RGB + HSV to select the closest color from MakeCode Arcade’s 16-color palette.
- **リサイズ / Resizing**：  
  ユーザー指定のピクセルサイズまたは、自動調整された最適なサイズ。  
  Uses user-specified pixel dimensions or automatically adjusts to the best size.
- **透明処理 / Transparency Handling**：  
  透明ピクセルは白 (`#FFFFFF`) に変換。  
  Transparent pixels are converted to white (`#FFFFFF`).

---

## 📝 注意点 / Notes
- 入力画像は `.png`, `.jpg`, `.jpeg` に対応。  
  Supported image formats: `.png`, `.jpg`, `.jpeg`
- 画像サイズが極端に小さい場合、適切な出力が得られない可能性があります。  
  If the input image is too small, the output may not be ideal.
- `pyperclip` を使用するため、クリップボード機能が動作しない場合は、手動でコピーしてください。  
  If `pyperclip` does not work, manually copy the output.

---

## 📜 ライセンス / License

このプロジェクトは WTFPL (Do What The Fuck You Want To Public License)のもとで提供されます。  
This project is licensed under the WTFPL (Do What The Fuck You Want To Public License)
### **LICENSE**
```txt
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE  
Version 2, December 2004  

Copyright (C) [Your Name]  

Everyone is permitted to copy and distribute verbatim or modified  
copies of this license document, and changing it is allowed as long  
as the name is changed.  

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE  
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION  

 0. You just DO WHAT THE FUCK YOU WANT TO.
```
