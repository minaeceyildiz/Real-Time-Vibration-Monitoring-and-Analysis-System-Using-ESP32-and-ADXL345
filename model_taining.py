import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sqlalchemy import create_engine
import joblib

# Veritabanı bağlantısı için SQLAlchemy engine oluşturma
engine = create_engine('mysql+mysqlconnector://root:@localhost/esp_data')

def fetch_data():
    query = "SELECT x, y, z, timestamp, status FROM classified_data ORDER BY timestamp DESC LIMIT 1000"
    df = pd.read_sql(query, engine)
    print("Fetched Data for Training:")
    print(df.head())  # Veriyi kontrol et
    return df

def preprocess_data(df):
    # Özellik ve hedef değişkenleri ayır
    X = df[['x', 'y', 'z']]
    y = df['status'].map({'Stable': 0, 'Vibrating': 1})
    
    print("Preprocessed Data:")
    print(X.head())  # Özellikleri kontrol et
    print(y.head())  # Hedef değişkeni kontrol et
    
    return X, y

def train_model(X_train, y_train):
    # Random Forest sınıflandırıcı oluştur
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Modeli eğit
    model.fit(X_train, y_train)
    
    return model

def evaluate_model(model, X_test, y_test):
    # Test verileri üzerinde tahmin yap
    y_pred = model.predict(X_test)
    
    # Modelin performansını değerlendir
    report = classification_report(y_test, y_pred)
    print("Model Performansı:\n", report)

def save_model(model, filename):
    # Modeli dosyaya kaydet
    joblib.dump(model, filename)
    print(f"Model {filename} olarak kaydedildi.")

def main():
    # Verileri çek
    df = fetch_data()
    
    # Verileri ön işleme tabi tut
    X, y = preprocess_data(df)
    
    # Eğitim ve test setlerine ayır
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Modeli eğit
    model = train_model(X_train, y_train)
    
    # Modeli değerlendir
    evaluate_model(model, X_test, y_test)
    
    # Modeli kaydet
    save_model(model, 'random_forest_model.pkl')

if __name__ == "__main__":
    main()
