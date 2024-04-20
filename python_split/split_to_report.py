import json
from bs4 import BeautifulSoup

# เปิดไฟล์ HTML
with open('scrapper.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# สร้างอ็อบเจ็กต์ BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# สร้างรายการเพื่อเก็บข้อมูล
data = []

# ค้นหาและตัดคำในแท็ก <p>
for paragraph in soup.find_all('span'):
    words = paragraph.get_text().split()  # แยกคำออกจากกัน
    data.append(words)

# เขียนข้อมูลเป็นไฟล์ JSON
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
