from lxml import html

# อ่านไฟล์ MHTML
with open('Gehenna Gate - Test _ Facebook.mhtml', 'rb') as f:
    mhtml_content = f.read()

# แปลง MHTML เป็น HTML
tree = html.fromstring(mhtml_content)
html_content = tree.xpath('//body')[0].text_content()

# บันทึกไฟล์ HTML
with open('converted_file.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('File converted successfully!')
