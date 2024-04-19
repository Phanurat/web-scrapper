<?php
// กำหนดตำแหน่งของไฟล์ MHTML
$file_path = 'C:/xampp/htdocs/web-scrapper/pdf/Gehenna%20Gate%20-%20Test%20_%20Facebook.mhtml';

// อ่านเนื้อหาของไฟล์ MHTML
$html_content = file_get_contents($file_path);

// ตรวจสอบว่าสามารถอ่านไฟล์ได้หรือไม่
if ($html_content !== false) {
    // ทำการแปลงเนื้อหา MHTML เป็น HTML หรือดำเนินการต่อตามต้องการ
    // ตัวอย่างเช่น: การใช้ HTML DOM Parser เพื่อดึงข้อมูลจากไฟล์ HTML
} else {
    echo 'Failed to read file.';
}
?>
