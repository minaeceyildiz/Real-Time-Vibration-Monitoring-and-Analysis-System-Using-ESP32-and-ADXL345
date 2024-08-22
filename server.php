<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
   
    $json = file_get_contents('php://input');
    $data = json_decode($json, true);

    
    $x = $data['x'];
    $y = $data['y'];
    $z = $data['z'];

    
    $servername = "localhost";
    $username = "root"; // Varsayılan XAMPP kullanıcı adı
    $password = ""; // Varsayılan olarak şifre boş
    $dbname = "esp_data";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "INSERT INTO vibration_data (x, y, z) VALUES ('$x', '$y', '$z')";

    if ($conn->query($sql) === TRUE) {
        echo "Veri başarıyla kaydedildi.";
    } else {
        echo "Hata: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
} else {
    echo "Invalid Request";
}
