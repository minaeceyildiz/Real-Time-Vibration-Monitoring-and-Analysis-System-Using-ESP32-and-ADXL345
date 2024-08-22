#include <WiFi.h>
#include <HTTPClient.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

// Wi-Fi bilgileri
const char* ssid = "Bren";
const char* password = "Bren2018";
const char* serverUrl = "http://192.168.212.115/my-server/server.php"; // Sunucu URL'si

// ADXL345 sensör nesnesi
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified();

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Bağlanıyor...");
    }
    Serial.println("Bağlandı!");

    // ADXL345 sensörünü başlatma
    if (!accel.begin()) {
        Serial.println("ADXL345 bulunamadı!");
        while (1);
    }
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        sensors_event_t event;
        accel.getEvent(&event); // Sensör verilerini alma

        // JSON verisi oluştur
        String jsonData = String("{\"x\":") + event.acceleration.x + 
                          String(",\"y\":") + event.acceleration.y + 
                          String(",\"z\":") + event.acceleration.z + "}";
        
        HTTPClient http; // HTTPClient nesnesi oluşturma
        http.begin(serverUrl); // Sunucu URL'sini tanımlama
        http.addHeader("Content-Type", "application/json"); // Başlık ekle

        // POST isteği gönder
        int httpResponseCode = http.POST(jsonData);

        if (httpResponseCode > 0) {
            String response = http.getString(); // Sunucudan gelen yanıt
            Serial.println("Yanıt: " + response);
        } else {
            Serial.print("Hata kodu: ");
            Serial.println(httpResponseCode);
        }
        
        http.end(); // İsteği sonlandır
    }

    delay(2000); // 2 saniye bekle
}