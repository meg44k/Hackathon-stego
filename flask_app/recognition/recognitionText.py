from google.cloud import vision
import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/mnt/c/Users/hinat/Documents/dev/stego-cup/test-konatan/cool-ascent-425906-b5-18c081794b5d.json'

def detect_text(path):
    """ファイル内のテキストを検出します。"""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    texts = response.text_annotations

    return texts[0].description if texts else ''

def extract_text_from_images(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(input_directory, filename)
            text = detect_text(image_path)

            text_file_name = os.path.splitext(filename)[0] + '.txt'
            text_file_path = os.path.join(output_directory, text_file_name)

            with open(text_file_path, 'w', encoding='utf-8') as file:
                file.write(text)

# 画像が含まれるディレクトリのパス（ローカル）
input_directory = '../uploads'

# テキストを保存するディレクトリのパス（ローカル）
output_directory = ''

extract_text_from_images(input_directory, output_directory)
