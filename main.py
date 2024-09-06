import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heart and Diabetes Interface")
        # Create buttons with images
        heart_image = tk.PhotoImage(file="image/heart.png")
        sugar_image = tk.PhotoImage(file="image/Diabetes.png")
        self.heart_button = tk.Button(self, image=heart_image, command=lambda: self.show_info_widget("heart"))
        self.heart_button.image = heart_image
        self.heart_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.sugar_button = tk.Button(self, image=sugar_image, command=lambda: self.show_info_widget("sugar"))
        self.sugar_button.image = sugar_image
        self.sugar_button.pack(side=tk.LEFT, padx=10, pady=10)
    def show_info_widget(self, button_type):
        if button_type == "heart":    
            self.info_widget = tk.Toplevel(self)
            self.info_widget.title("Fill out information")
            # Create fields
            tk.Label(self.info_widget, text="Enter age:").pack()
            self.age_entry = tk.Entry(self.info_widget)
            self.age_entry.pack()
            tk.Label(self.info_widget, text="Enter gender:").pack()
            self.gender_var = tk.StringVar()
            self.gender_var.set("male")  # default value
            tk.OptionMenu(self.info_widget, self.gender_var, "male", "female").pack()
            tk.Label(self.info_widget, text="Enter the type of chest pain:").pack()
            self.chest_pain_var = tk.StringVar()
            self.chest_pain_var.set("ATA")  # default value
            tk.OptionMenu(self.info_widget, self.chest_pain_var, "ATA", "NAP", "ASY", "TA").pack()
            tk.Label(self.info_widget, text="Enter your resting blood pressure:").pack()
            self.blood_pressure_entry = tk.Entry(self.info_widget)
            self.blood_pressure_entry.pack()
            tk.Label(self.info_widget, text="Enter cholesterol:").pack()
            self.cholesterol_entry = tk.Entry(self.info_widget)
            self.cholesterol_entry.pack()
            tk.Label(self.info_widget, text="Enter your fasting blood sugar:").pack()
            self.blood_sugar_entry = tk.Entry(self.info_widget)
            self.blood_sugar_entry.pack()
            tk.Label(self.info_widget, text="Enter resting ECG:").pack()
            self.ecg_var = tk.StringVar()
            self.ecg_var.set("Normal")  # default value
            tk.OptionMenu(self.info_widget, self.ecg_var, "Normal", "ST", "LVH").pack()
            tk.Label(self.info_widget, text="Enter your maximum heart rate:").pack()
            self.heart_rate_entry = tk.Entry(self.info_widget)
            self.heart_rate_entry.pack()
            tk.Label(self.info_widget, text="Enter angina exercise:").pack()
            self.angina_var = tk.StringVar()
            self.angina_var.set("N")  # default value
            tk.OptionMenu(self.info_widget, self.angina_var, "N", "Y").pack()
            tk.Label(self.info_widget, text="Enter the ancient peak:").pack()
            self.ancient_peak_entry = tk.Entry(self.info_widget)
            self.ancient_peak_entry.pack()
            tk.Label(self.info_widget, text="Enter ST slope:").pack()
            self.st_slope_var = tk.StringVar()
            self.st_slope_var.set("up")  # default value
            tk.OptionMenu(self.info_widget, self.st_slope_var, "up", "flat", "down").pack()
            # Create clear button
            self.clear_button = tk.Button(self.info_widget, text="Start the scan", command=lambda: self.send_info(button_type))
            self.clear_button.pack(pady=10)
        else:
            self.info_widget = tk.Toplevel(self)
            self.info_widget.title("Fill out information")
            # Create fields
            tk.Label(self.info_widget, text="Enter Pregnancies:").pack()
            self.Pregnancies_entry = tk.Entry(self.info_widget)
            self.Pregnancies_entry.pack()
            tk.Label(self.info_widget, text="Enter Glucose:").pack()
            self.Glucose_entry = tk.Entry(self.info_widget)
            self.Glucose_entry.pack()
            tk.Label(self.info_widget, text="Enter BloodPressure:").pack()
            self.BloodPressure_entry = tk.Entry(self.info_widget)
            self.BloodPressure_entry.pack()
            tk.Label(self.info_widget, text="Enter SkinThickness:").pack()
            self.SkinThickness_entry = tk.Entry(self.info_widget)
            self.SkinThickness_entry.pack()
            tk.Label(self.info_widget, text="Enter Insulin:").pack()
            self.Insulin_entry = tk.Entry(self.info_widget)
            self.Insulin_entry.pack()
            tk.Label(self.info_widget, text="Enter BMI:").pack()
            self.BMI_entry = tk.Entry(self.info_widget)
            self.BMI_entry.pack()
            tk.Label(self.info_widget, text="Enter DiabetesPedigreeFunction:").pack()
            self.DiabetesPedigreeFunction_entry = tk.Entry(self.info_widget)
            self.DiabetesPedigreeFunction_entry.pack()
            tk.Label(self.info_widget, text="Enter Age:").pack()
            self.age_entry = tk.Entry(self.info_widget)
            self.age_entry.pack()
            self.clear_button = tk.Button(self.info_widget, text="Start the scan", command=lambda: self.send_info(button_type))
            self.clear_button.pack(pady=10)

    def send_info(self, button_type):
        
        if button_type == "heart":
            age = self.age_entry.get()
            gender = self.gender_var.get()
            chest_pain = self.chest_pain_var.get()
            blood_pressure = self.blood_pressure_entry.get()
            cholesterol = self.cholesterol_entry.get()
            blood_sugar = self.blood_sugar_entry.get()
            ecg = self.ecg_var.get()
            heart_rate = self.heart_rate_entry.get()
            angina = self.angina_var.get()
            ancient_peak = self.ancient_peak_entry.get()
            st_slope = self.st_slope_var.get()
        
            result = heart_function(age, gender, chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, heart_rate, angina, ancient_peak, st_slope)

        
        else:
            Pregnancies = self.Pregnancies_entry.get()
            Glucose = self.Glucose_entry.get()
            BloodPressure = self.BloodPressure_entry.get()
            SkinThickness = self.SkinThickness_entry.get()
            Insulin = self.Insulin_entry.get()
            BMI = self.BMI_entry.get()
            DiabetesPedigreeFunction = self.DiabetesPedigreeFunction_entry.get()
            Age = self.age_entry.get()
            result = sugar_function(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        messagebox.showinfo("Result", str(result))

def sugar_function(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    data = pd.read_csv("Database/diabetes.csv")
    data.head()
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = SVC(kernel='linear', C=0.1, random_state=42)
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = SVC(kernel="linear", C=1.0, random_state=42)
    model.fit(X_train, y_train)
    patient_data = {
    "Pregnancies": Pregnancies,
    "Glucose": Glucose,
    "BloodPressure": BloodPressure,
    "SkinThickness": SkinThickness,
    "Insulin": Insulin,
    "BMI": BMI,
    "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
    "Age": Age,
    }
    patient_df = pd.DataFrame(patient_data, index=[0])
    prediction = model.predict(patient_df)

    print("Patient data:")
    print(patient_df)

    if prediction[0] == 1:
        print("Diabetes detected.")
        return "Diabetes detected."
    else:
        print("Normal.")
        return "Normal."



def heart_function(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):   
    data = pd.read_csv("Database/heart.csv")
    data.head()
    missing_value =  data.isnull().any(axis=1)
    print("mising value")
    print(missing_value)
    data.shape
    categori = {
        "ChestPainType": ['ATA', 'NAP', 'ASY', 'TA'],
        "Sex": ['M', 'F'],
        "RestingECG": ['Normal', 'ST', 'LVH'],
        "ExerciseAngina": ['N', 'Y'],
        "ST_Slope": ['Up', 'Flat', 'Down'],
    }
    
    X = data.drop("HeartDisease", axis=1)
    y = data["HeartDisease"]
    X = pd.get_dummies(X, columns=categori.keys())
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logistic_classifier = LogisticRegression()
    logistic_classifier.fit(X_train, y_train)
    patient_data = {
        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain_type,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope,
    }
    patient_df = pd.DataFrame([patient_data])
    patient_df = pd.get_dummies(patient_df, columns=categori.keys())
    missing_features = set(X_test.columns) - set(patient_df.columns)
    for feature in missing_features:
        patient_df[feature] = 0
    patient_df = patient_df[X_test.columns]
    prediction = logistic_classifier.predict(patient_df)
    if prediction[0] == 1:
        print("Heart disease detected.")
        return "Heart disease detected."
    else:
        print("Heart disease not detected (normal).")
        return "Heart disease not detected (normal)."
if __name__ == "__main__":
    app = Application()
    app.mainloop()
