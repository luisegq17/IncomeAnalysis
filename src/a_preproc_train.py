d1={
    "l1":[
        "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",
        "Local-gov", "State-gov", "Without-pay", "Never-worked", "?"
    ],
    "l3":[
        "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school",
        "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters",
        "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool", "?"
    ],
    "l5":[
        "Married-civ-spouse", "Divorced", "Never-married", "Separated",
        "Widowed", "Married-spouse-absent", "Married-AF-spouse", "?"
    ],
    "l6":[
        "Tech-support", "Craft-repair", "Other-service", "Sales",
        "Exec-managerial", "Prof-specialty", "Handlers-cleaners",
        "Machine-op-inspct", "Adm-clerical", "Farming-fishing",
        "Transport-moving", "Priv-house-serv", "Protective-serv",
        "Armed-Forces", "?"
    ],
    "l7":[
        "Wife", "Own-child", "Husband", "Not-in-family",
        "Other-relative", "Unmarried", "?"
    ],
    "l8":[
        "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo",
        "Other", "Black", "?"
    ],
    "l9":[
        "Female", "Male", "?"
    ],
    "l13":[
        "United-States", "Cambodia", "England", "Puerto-Rico",
        "Canada", "Germany", "Outlying-US(Guam-USVI-etc)",
        "India","Japan", "Greece", "South", "China", "Cuba", "Iran",
        "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam",
        "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic",
        "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala",
        "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador",
        "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands", "?"
    ],
    "l14":[
        "<=50K\n", ">50K\n"
    ]
}

def f0(v1,ln):
    r1=0
    lns="l"+str(ln)
    c=0
    for i in d1[lns]:
        if(v1==i):
            r1=c
        c+=1
    return(r1)