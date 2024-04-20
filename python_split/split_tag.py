from bs4 import BeautifulSoup

# เปิดไฟล์ HTML
with open('scrapper.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# สร้างอ็อบเจ็กต์ BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# ค้นหาและตัดคำในแท็ก <p>
for paragraph in soup.find_all('span'):
    words = paragraph.get_text().split()  # แยกคำออกจากกัน
    print(words)  # พิมพ์รายการคำที่ถูกตัดออกมา

