import pandas as pd
import joblib
from sqlalchemy import create_engine

# Veritabanı bağlantısı için SQLAlchemy engine oluşturma
engine = create_engine('mysql+mysqlconnector://root:@localhost/esp_data')

def fetch_new_data():
    # Yeni verileri veritabanından al
    query = "SELECT x, y, z, timestamp FROM vibration_data ORDER BY timestamp DESC LIMIT 100"
    df = pd.read_sql(query, engine)
    print("Fetched New Data:")
    print(df.head())  # Yeni veriyi kontrol et
    return df

def load_model(filename):
    # Eğitilmiş modeli yükle
    model = joblib.load(filename)
    return model

def predict_data(df, model):
    # Yeni veriler üzerinde tahmin yap
    predictions = model.predict(df[['x', 'y', 'z']])
    df['status'] = ['Stable' if pred == 0 else 'Vibrating' for pred in predictions]
    print("Predictions:")
    print(df.head())  # Tahmin sonuçlarını kontrol et
    return df

def save_predictions(df):
    # Tahmin sonuçlarını veritabanına kaydet
    df.to_sql('classified_data', con=engine, if_exists='append', index=False)

def main():
    # Yeni verileri al
    df = fetch_new_data()
    
    # Modeli yükle
    model = load_model('random_forest_model.pkl')
    
    # Veriler üzerinde tahmin yap
    df = predict_data(df, model)
    
    # Tahminleri veritabanına kaydet
    save_predictions(df)
    print("Tahminler yapıldı ve veritabanına kaydedildi.")

if __name__ == "__main__":
    main()
