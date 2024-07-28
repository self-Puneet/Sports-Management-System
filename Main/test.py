# import firebase_admin
# from firebase_admin import credentials, firestore

# key = "C:\Users\punee\Downloads\sports-maagement-database-firebase-adminsdk-j2q72-a620bd1e37.json"
# cred = credentials.Certificate(key)
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# # Write sample data to Firestore
# doc_ref = db.collection('sports').document('player1')
# doc_ref.set({
#     'name': 'John Doe',
#     'age': 25,
#     'team': 'Lakers',
#     'position': 'Forward'
# })

# print("Data written to Firestore successfully.")


dict = {1:2, 3:4}
if 1 in dict.keys(): print("true")
print(dict[1])
print(list(dict.keys())[0])


"""
        # Reference to the specific document
        doc_ref = db.collection('credentials').document('login_database')
            
        # Get the document
        doc = doc_ref.get()

        data = doc.to_dict()

"""