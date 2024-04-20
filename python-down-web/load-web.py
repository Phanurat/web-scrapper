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
url = 'https://www.facebook.com/aseanfootball/posts/pfbid033GHRZKjECRCBaaqNbpDij8wXkXZ4JKPMF7VrGq6WDDEKN37nTnk8eu4UP8t5M4kUl'
filename = 'football-save.html'

# เรียกใช้ฟังก์ชันเพื่อดาวน์โหลดและบันทึกเว็บไซต์
download_complete_webpage(url, filename)
