import requests

def extract_image_links(html_text):
    i_start = None
    i_end = None
    result = []
    for i, l in enumerate(html_text):
        if l == '\'' and not i_start:
            i_start = i + 1
        elif l == '\'':
            i_end = i
            result.append(html_text[i_start:i_end])
            i_start = None
    return result




sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"
image_links = extract_image_links(sample_html)
if image_links:
  for image_link in image_links:
    print(image_link)
else:
  print("Нет ссылок с картинками в HTML тексте.")