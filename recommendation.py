import joblib
import pandas as pd


def main():
    # Load the trained model
    model_file = 'crop_recommendation_model.pkl'
    model = joblib.load(model_file)

    # Load the dataset
    dataset_file = 'soil_measures.csv'
    dataset = pd.read_csv(dataset_file)

    # Predict the crop
    recommended_crop = model.predict(dataset[['K']])
    recommended_crop = pd.Series(recommended_crop).mode()[0]

    print(f"The recommended crop based on the dataset is: {recommended_crop}")


if __name__ == "__main__":
    main()
