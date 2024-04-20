from bs4 import BeautifulSoup

# เปิดไฟล์ HTML
with open('scrapper.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# สร้างอ็อบเจ็กต์ BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# สร้างเซ็ตเพื่อเก็บคำศัพท์ที่เราพบ
unique_words = set()

# สร้างเซ็ตเพื่อเก็บคำศัพท์ที่ปรากฏซ้ำมากกว่า 3 ครั้ง
repeated_words = set()

# ค้นหาและเพิ่มคำศัพท์ในแท็ก <span> เข้าสู่เซ็ต
for paragraph in soup.find_all('span'):
    words = paragraph.get_text().split()  # แยกคำออกจากกัน
    #words = paragraph.get_text()
    for word in words:
        if word in unique_words:
            repeated_words.add(word)
        else:
            unique_words.add(word)

# พิมพ์คำที่ซ้ำมากกว่า 3 คำขึ้นไป
print("คำที่ซ้ำมากกว่า 3 คำขึ้นไป:")
for word in repeated_words:
    print(word)
