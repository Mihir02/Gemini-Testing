from dotenv import load_dotenv
import PIL.Image
import os

def convert_text_to_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    # Join lines into a single string
    text_string = ' '.join(lines)

    # Replace newline characters with a space
    text_string = text_string.replace('\n', ' ')

    # Replace multiple spaces with a single space
    text_string = ' '.join(text_string.split())

    # Add space after every dot before a new question
    text_string = text_string.replace('.', '. ')

    return text_string

file_path = './prompt.txt'
formatted_text = convert_text_to_string(file_path)


load_dotenv()  # This line brings all environment variables from .env into os.environ

import google.generativeai as genai

genai.configure(api_key = os.environ['GEMINI_API'])

model = genai.GenerativeModel('gemini-1.5-pro')

img = PIL.Image.open('picture_design.jpg')
img2 = PIL.Image.open('pic_mobile.jpg')

response = model.generate_content([formatted_text, img, img2])
response.resolve()

print(response.text)