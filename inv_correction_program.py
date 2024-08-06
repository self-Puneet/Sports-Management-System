
import firebase_admin
from firebase_admin import credentials, firestore

# connecting to firebase.
key = r"C:\Users\punee\Downloads\sports-management-database-firebase-adminsdk-j2q72-a620bd1e37.json"
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)
db = firestore.client()

dict = {
    "badminton" : {
        "i_badminton_racquet" : 6,
        "i_shuttle" : 48,
        "i_badminton_net" : 6
    },
    "basketball" : {
        "i_basketball" : 8
    },
    "carrom" : {
        "i_carrom_striker" : 6,
        "i_carrom_board" : 5,
        "i_carrom_coins" : 5,
        "i_carrom_powder" : 2
    },
    "chess" : {
        "i_chessboard_wooden" : 4,
        "i_chessboard_pvc" : 3,
        "i_chessmen" : 4
    },
    "cricket" : {
        "i_keeping_pad" : 6,
        "i_bails" : 10,
        "i_cricket_elbow_guard" : 4,
        "i_cricket_kit_bag" : 1,
        "i_stumps" : 12,
        "i_cricket_ball_leather" : 20,
        "i_cricket_bat" : 3,
        "i_cricket_matting" : 2,
        "i_cricket_ball_tennis" : 18,
        "i_keeping_gloves" : 8,
        "i_batting_gloves" : 12,
        "i_abdominal_guard" : 9,
        "i_batting_pad" : 21,
        "i_cricket_helmet" : 4,
    },
    "football" : {
        "i_knee_cap" : 6,
        "i_shing_guard" : 8,
        "i_keeping_gloves" : 4,
        "i_football" : 6,
    },
    "lawn_tennis" : {
        "i_lawn_tennis_racquet" : 6,
        "i_lawn_tennis_ball" : 6
    },
    "miscellaneous" : {
        "i_cones" : 20,
        "i_shot_put" : 2,
        "i_yoga_mat" : 10,
        "i_skipping_rope" : 8,
        "i_air_pump" : 2,
        "i_disc_throw" : 4,
        "i_markers" : 20,
        "i_javelin" : 3,
        "i_madicine_ball" : 4 
    },
    "table_tennis" : {
        "i_table_tennis_ball" : 12,
        "i_table_tennis_bat" : 12
    },
    "volleyball" : {
        "i_volleyball" : 6
    }
}

for i in dict:
    db.collection("preErp").document(i).set(dict[i])   