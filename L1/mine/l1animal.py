topology = [('Animal', 'Environment'), 
                   ('Animal', 'HasShell'),
                   ('Animal', 'Class'),
                   ('Animal', 'BearsYoungAs'),
                   ('Class', 'WarmBllooded'),
                   ('Class', 'BodyCovering')]
data = {
        "Animal": {
            "Monkey": [0, 2],
            "Penguin": [0, 2],
            "Platypus": [0, 2],
            "Robin": [0, 2],
            "Turtle": [0, 2]
        },
        "Environment": {
            "Monkey": {"Air": 0, "Land": 1, "Water": 0},
            "Penguin": {"Air": 0, "Land": 0.5, "Water": 0.5},
            "Platypus": {"Air": 0, "Land": 0, "Water": 1},
            "Robin": {"Air": 0.5, "Land": 0.5, "Water": 0},
            "Turtle": {"Air": 0, "Land": 0.5, "Water": 0.5}
        },
        "HasShell": {
            "Monkey": {"True": 0, "False": 1},
            "Penguin": {"True": 0, "False": 1},
            "Platypus": {"True": 0, "False": 1},
            "Robin": {"True": 0, "False": 1},
            "Turtle": {"True": 1, "False": 0}
        },
        "BearsYoungAs": {
            "Monkey": {"Live": 1, "Eggs": 0},
            "Penguin": {"Live": 0, "Eggs": 1},
            "Platypus": {"Live": 0, "Eggs": 1},
            "Robin": {"Live": 0, "Eggs": 1},
            "Turtle": {"Live": 0, "Eggs": 1}
        },
        "Class": {
            "Monkey": {"Bird": 0, "Mammal": 1, "Reptile": 0},
            "Penguin": {"Bird": 1, "Mammal": 0, "Reptile": 0},
            "Platypus": {"Bird": 0, "Mammal": 1, "Reptile": 0},
            "Robin": {"Bird": 1, "Mammal": 0, "Reptile": 0},
            "Turtle": {"Bird": 0, "Mammal": 0, "Reptile": 1}
        },
        "WarmBlooded": {
            "Bird": {"True": 1, "False": 0},
            "Mammal": {"True": 1, "False": 0},
            "Reptile": {"True": 0, "False": 1}
        },
        "BodyCovering": {
            "Bird": {"Fur": 0, "Feathers": 1, "Scales": 0},
            "Mammal": {"Fur": 1, "Feathers": 0, "Scales": 0},
            "Reptile": {"Fur": 0, "Feathers": 0, "Scales": 1}
        }
}