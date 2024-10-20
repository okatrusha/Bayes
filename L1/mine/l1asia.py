netwrok = "Asia"

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
        "VisitAsia": {
            "Visit": {"Present": 0.05, "Absent": 0.95},
            "NoVisit": {"Present": 0.01, "Absent": 0.99}
        }
    },
    "LungCancer": {
        "Smoking": {
            "Smoking": {"Present": 0.1, "Absent": 0.9},
            "NoSmoking": {"Present": 0.01, "Absent": 0.99}
        }
    },
    "Tb_or_Ca": {
        "Tuberculosis": {
            "Present": {
                "Lung Cancer": {"Present": {"True": 1, "False": 0},
                                "Absent": {"True": 1, "False": 0}
                },
            },
            "Absent": {
                "Lung Cancer": {"Present": {"True": 1, "False": 0},
                                "Absent": {"True": 0, "False": 1}
                }
            }
        }
    },
    "XRay": {
        "Tb_or_Ca": {
            "True": {"Abnormal": 0.98, "Normal": 0.02},
            "False": {"Abnormal": 0.05, "Normal": 0.95}
        }
    },
    "Bronchitis": {
        "Smoking": {
            "Smoking": {"Present": 0.6, "Absent": 0.4},
            "NoSmoking": {"Present": 0.3, "Absent": 0.7}
        }
    },
    "Dyspnea": {
        "Tb_or_Ca": {
            "True": {
                "Bronchitis": {
                    "Present": {"True": 0.9, "False": 0.1},
                    "Absent": {"True": 0.7, "False": 0.3}
                }
            },
            "False": {
                "Bronchitis": {
                    "Present": {"True": 0.8, "False": 0.2},
                    "Absent": {"True": 0.1, "False": 0.9}
                }
            }
        }
    }
}
