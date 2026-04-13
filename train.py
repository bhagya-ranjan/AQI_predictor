import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


def load_data():
    return pd.read_csv("data/city_day.csv")


def preprocess(df):
    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day

    # Drop unnecessary columns
    df = df.drop(['Date', 'AQI_Bucket'], axis=1)

    # One-hot encode City
    df = pd.get_dummies(df, columns=['City'], drop_first=True)

    # Fill missing values (only numeric)
    df = df.fillna(df.mean(numeric_only=True))

    return df


def train_model(df):
    X = df.drop("AQI", axis=1)
    y = df["AQI"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestRegressor(n_estimators=50, max_depth=15)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"RMSE: {rmse:.2f}")
    print(f"R2 Score: {r2:.4f}")

    return model, scaler, X.columns


def save_artifacts(model, scaler, columns):
    os.makedirs("model", exist_ok=True)

    with open("model/model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("model/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    with open("model/columns.pkl", "wb") as f:
        pickle.dump(columns, f)

    print("Model, scaler, and columns saved successfully!")


def main():
    print("Loading data...")
    df = load_data()

    print("Preprocessing data...")
    df = preprocess(df)

    print("Training model...")
    model, scaler, columns = train_model(df)

    print("Saving model files...")
    save_artifacts(model, scaler, columns)

    print("✅ Training complete!")


if __name__ == "__main__":
    main()