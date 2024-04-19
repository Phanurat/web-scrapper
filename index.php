<?php
// รวมไฟล์ของ Simple HTML DOM Parser
require 'simple_html_dom.php';
require __DIR__ . '/vendor/autoload.php';

// ใช้ GuzzleHTTP เพื่อส่งคำขอ HTTP
use GuzzleHttp\Client;

// กำหนด URL ของหน้าเว็บที่ต้องการดึงข้อมูล
$url = 'https://www.facebook.com/permalink.php?story_fbid=pfbid0JvNH5iWUciSDkHJxQpiqkvWsMqLtGTCvbVnm8qXmD7tuxXrsqeHb1MAUSmx5s2uzl&id=61558499640631';

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
    foreach($html->find('div[class=x169t7cy x19f6ikt]') as $element) {
        // แสดงเนื้อหาที่ดึงได้

        //echo "Test";
        echo "Connect Successfully!"."<br>";
        echo "Content Comment=>". $element->plaintext . "<br>";
    }
} else {
    echo 'Failed to retrieve page. Status code: ' . $response->getStatusCode();
    echo "Test Error";
}
?>
