trains = [
    {
        'no':0,
        'name': 'New Delhi - Chandigarh Shatabdi Express',
        'stations': ['Panipat Junction', 'Kurukshetra Junction', 'Ambala Cant Junction', 'Chandigarh Junction'],
        'distances': [90000, 157000, 199000,244000],
        
    },
    {
        'no':1,
        'name': 'New Delhi - Shri Mata Vaishno Devi Katra Vande Bharat Express',
        'stations':['Ambala Cantt Junction', 'Ludhiana Junction', 'Jammu Tawi','Katra Junction'],
        'distances': [199000, 313000 ,577000 ,655000],
    },
    {
        'no':2,
        'name': 'New Delhi - Lucknow Jn. Swarn Shatabdi Express',
        'stations': ['Ghaziabad Junction', 'Aligarh Junction', 'Tundla Junction', 'Etawah Junction', 'Kanpur Central','Lucknow Junction'],
        'distances': [25000,131000,209000,301000,440000,512000],
    }

]
map = [
    {
       'pathlist':[(28.668599920844756, 77.20044427610303),(28.994171577218825, 77.01441420757034), (29.413128099019627, 76.96481089994793), (29.99229637203275, 76.86211939091326),(29.98160834083052, 76.84663127808665),(30.70643990617078, 76.82081632927672)],
       'destination':'Chandigarh'
    },
    {
        'pathlist':[(28.647477413807085, 77.21923309540645),(29.008501001319956, 77.00719128155002),(29.390892417574307, 76.96724197686724),(29.971790134963452, 76.87303278382643),(30.33686198700739, 76.84084198670121),(30.37691332893945, 76.78050667047056),(30.906680923588183, 75.85207903683359),(31.236077435905173, 75.7680137929943),(31.330695752363734, 75.6118718725958),(32.12057861453503, 75.61323112400018),(32.73323255479599, 74.86899885341859),(32.7819813247474, 75.14400749524943),(32.995932347986425, 74.92831444283308)],
        'destination':'Katra Jammu'
    },
    {
        'pathlist':[(28.682954447789072, 77.11100271778183),(28.66852854383702, 77.39938059314296),(27.912423182154242, 78.0977513667463),(27.221673693326455, 78.18939202882956),(27.230115427947, 78.20837912958129),(26.455063401536712, 80.34679811554676),(26.830546097075725, 80.94726426858115)],
        'destination':'Lucknow'
    }
]

sard = [
    {
     'topspeed':36.11,
     'accelerationsun':[2,4,8,16],
     'accelerationrain':[2,4],
     'retardationsun':[3,5,7,10],
     'retardationrain':[3,5]

    },
    {
     'topspeed':50,
     'accelerationsun':[5,10,15,20],
     'accelerationrain':[5,10],
     'retardationsun':[3,6,9,12],
     'retardationrain':[3,6]
    },
    {
      'topspeed':36.11,
     'accelerationsun':[2,4,8,16],
     'accelerationrain':[2,4],
     'retardationsun':[3,5,7,10],
     'retardationrain':[3,5]
    }
]

