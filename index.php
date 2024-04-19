<?php

// รวมไฟล์ของ Simple HTML DOM Parser
require 'simple_html_dom.php';
require __DIR__ . '/vendor/autoload.php';

// ใช้ GuzzleHTTP เพื่อส่งคำขอ HTTP
use GuzzleHttp\Client;

// กำหนด URL ของหน้าเว็บที่ต้องการดึงข้อมูล
$url = 'https://web.facebook.com/permalink.php?story_fbid=pfbid02NwxzZXi3HcGJ2K32LAQ5rWKYk9HH18uSMKkdgng3KUbNBkaGkYqQaMFfVYStdBAul&id=61558499640631';

// สร้างอ็อบเจ็กต์ของ GuzzleHTTP Client
$client = new Client();

// ส่งคำขอ GET เพื่อดึงเนื้อหาของหน้า
$response = $client->request('GET', $url);

// ตรวจสอบสถานะการตอบกลับของคำขอ
if ($response->getStatusCode() == 200) {
    // ดึงข้อมูล HTML จากเนื้อหาของคำตอบ
    $html_content = (string) $response->getBody();
    
    // สร้างอ็อบเจ็กต์ของ Simple HTML DOM Parser
    $html = str_get_html($html_content);
    
    // ค้นหาและดึงข้อมูลตามต้องการ
    foreach($html->find('div[class=xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs]') as $element) {
        // แสดงเนื้อหาที่ดึงได้
        echo $element->plaintext . "<br>";
    }
} else {
    echo 'Failed to retrieve page. Status code: ' . $response->getStatusCode();
}
?>
