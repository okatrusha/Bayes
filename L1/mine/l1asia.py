netwrok = "asia"

topology = [('VisitAsia', 'Tuberculosis'), 
                   ('Tuberculosis', 'Tb_or_Ca'),
                   ('Animal', 'Class'),
                   ('Smoking', 'LungCancer'),
                   ('LungCancer', 'Tb_or_Ca'),
                   ('Tb_or_Ca', 'XRay'),
                   ('Tb_or_Ca', 'Dyspnea'),
                   ('Bronchitis', 'Dyspnea'),
                   ('Smoking', 'Bronchitis')
                   ]

data = {
    "VisitAsia": {
        "Visit": 0.01,
        "NoVisit": 0.99
    },
    "Smoking": {
        "Smoking": 0.5,
        "NoSmoking": 0.5
    },
    "Tuberculosis": {
        "Present": {
            "VisitAsia.Visit": 0.05,
            "VisitAsia.NoVisit": 0.01
        },
        "Absent": {
            "VisitAsia.Visit": 0.95,
            "VisitAsia.NoVisit": 0.99
        }
    },
    "LungCancer": {
        "Present": {
            "Smoking.Smoking": 0.1,
            "Smoking.NoSmoking": 0.01
        },
        "Absent": {
            "Smoking.Smoking": 0.9,
            "Smoking.NoSmoking": 0.99
        }
    },
    "Tb_or_Ca": {
        "True": {
            "Tuberculosis.Present,LungCancer.Present": 1,
            "Tuberculosis.Present,LungCancer.Present": 1,
            "Tuberculosis.Absent,LungCancer.Present": 1,
            "Tuberculosis.Absent,LungCancer.Absent": 0
            },
        "False": {
            "Tuberculosis.Present,LungCancer.Present": 0,
            "Tuberculosis.Present,LungCancer.Present": 0,
            "Tuberculosis.Absent,LungCancer.Present": 0,
            "Tuberculosis.Absent,LungCancer.Absent": 1
            }
    },

    "XRay": {
        "Abnormal": {
            "Tb_or_Ca.True": 0.98,
            "Tb_or_Ca.False": 0.05
        },
        "Normal": {
            "Tb_or_Ca.True": 0.02,
            "Tb_or_Ca.False": 0.95
        }
    },
    "Bronchitis": {
        "Present": {
            "Smoking.Smoking": 0.6,
            "Smoking.NoSmoking": 0.3
        },
        "Absent": {
            "Smoking.Smoking": 0.4,
            "Smoking.NoSmoking": 0.7
        }
    },
    "Dyspnea": {
        "True": {
            "Tb_or_Ca.True,Bronchitis.Present": 0.9,
            "Tb_or_Ca.True,Bronchitis.Absent": 0.7,
            "Tb_or_Ca.False,Bronchitis.Present": 0.8,
            "Tb_or_Ca.False,Bronchitis.Absent": 0.1
            },
        "False": {
            "Tb_or_Ca.True,Bronchitis.Present": 0.1,
            "Tb_or_Ca.True,Bronchitis.Absent": 0.3,
            "Tb_or_Ca.False,Bronchitis.Present": 0.2,
            "Tb_or_Ca.False,Bronchitis.Absent": 0.9
            }
    }
}

