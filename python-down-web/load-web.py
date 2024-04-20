import requests
from bs4 import BeautifulSoup

def download_complete_webpage(url, filename):
    # ดึงข้อมูล HTML จาก URL
    response = requests.get(url)
    html_content = response.text

    # เข้าถึงข้อมูล HTML ด้วย BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # บันทึกเป็นไฟล์ HTML
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# ระบุ URL และชื่อไฟล์ที่ต้องการบันทึก
url = 'https://www.facebook.com/permalink.php?story_fbid=pfbid0JvNH5iWUciSDkHJxQpiqkvWsMqLtGTCvbVnm8qXmD7tuxXrsqeHb1MAUSmx5s2uzl&id=61558499640631'
filename = 'complete_webpage.html'

# เรียกใช้ฟังก์ชันเพื่อดาวน์โหลดและบันทึกเว็บไซต์
download_complete_webpage(url, filename)
