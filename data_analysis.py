from sqlalchemy import create_engine
import pandas as pd
import numpy as np

# Veritabanı bağlantısı için SQLAlchemy engine oluşturma
engine = create_engine('mysql+mysqlconnector://root:@localhost/esp_data')

def fetch_data():
    query = "SELECT x, y, z, timestamp FROM vibration_data ORDER BY timestamp DESC LIMIT 100"
    df = pd.read_sql(query, engine)
    print("Fetch Data:")
    print(df.head())  # Veriyi kontrol et
    return df

def classify_data(df):
    # Varsayılan olarak tüm verileri 'Stable' olarak sınıflandır
    df['status'] = 'Stable'
    
    # X, Y ve Z eksenlerindeki standart sapmayı hesapla
    df['std'] = df[['x', 'y', 'z']].std(axis=1)
    
    # Standart sapma belirli bir eşikten büyükse 'Vibrating' olarak işaretle
    df.loc[df['std'] > 1.0, 'status'] = 'Vibrating'  # Eşik değeri 1.0 olarak artırıldı
    
    print("Classified Data:")
    print(df.head())  # Sınıflandırılmış veriyi kontrol et
    return df

def save_classified_data(df):
    df.to_sql('classified_data', con=engine, if_exists='append', index=False)

def main():
    df = fetch_data()
    df = classify_data(df)
    save_classified_data(df)
    print("Veri analizi tamamlandı ve veritabanına kaydedildi.")

if __name__ == "__main__":
    main()
