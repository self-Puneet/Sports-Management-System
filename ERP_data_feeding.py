import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# connecting to firebase.
key = r"C:\Users\punee\Downloads\login-lakshh-firebase-adminsdk-hu91e-5712af1dcf.json"
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)
db = firestore.client()




# Replace 'students.csv' with the path to your CSV file
file_path = 'ERP data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)


fields_to_remove = ["S.No.", "Session (Admission)" ,"Specialization In"]  # Add the columns you want to remove
df.drop(columns=fields_to_remove, inplace=True)


# Convert the DataFrame to a nested list
students_list = df.values.tolist()




attribute_list = ["college", "enroll_no", "name", "program", "sem", "phone_no", "email"]

data = {}
for i in range(0, len(students_list)):
    dict_data = {}
    for j in range(0, len(students_list[i])):
        dict_data[attribute_list[j]] = students_list[i][j]
    db.collection("preErp").document(dict_data["email"]).set(dict_data)
