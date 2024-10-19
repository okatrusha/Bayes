topology = [('Animal', 'Environment'), 
                   ('Animal', 'HasShell'),
                   ('Animal', 'Class'),
                   ('Animal', 'BearsYoungAs'),
                   ('Class', 'WarmBlooded'),
                   ('Class', 'BodyCovering')]
data = {
        "Animal": {
            "Monkey": 0.2,
            "Penguin": 0.2,
            "Platypus": 0.2,
            "Robin": 0.2,
            "Turtle": 0.2
        },
        "Environment": {
            "Air": {
                "Monkey": 0,
                "Penguin": 0,
                "Platypus": 0,
                "Robin": 0.5,
                "Turtle": 0
            },
            "Land": {
                "Monkey": 1,
                "Penguin": 0.5,
                "Platypus": 0,
                "Robin": 0.5,
                "Turtle": 0.5
            },
            "Water": {
                "Monkey": 0,
                "Penguin": 0.5,
                "Platypus": 1,
                "Robin": 0,
                "Turtle": 0.5
            }
        },
        "HasShell": {
            "True": {
                "Monkey": 0,
                "Penguin": 0,
                "Platypus": 0,
                "Robin": 0,
                "Turtle": 1
            },
            "False": {
                "Monkey": 1,
                "Penguin": 1,
                "Platypus": 1,
                "Robin": 1,
                "Turtle": 0
            }
        },
        "BearsYoungAs": {
            "Live": {
                "Monkey": 1,
                "Penguin": 0,
                "Platypus": 0,
                "Robin": 0,
                "Turtle": 0
            },
            "Eggs": {
                "Monkey": 0,
                "Penguin": 1,
                "Platypus": 1,
                "Robin": 1,
                "Turtle": 1
            }
        },
        "Class": {
            "Bird": {
                "Monkey": 0,
                "Penguin": 1,
                "Platypus": 0,
                "Robin": 1,
                "Turtle": 0
            },
            "Mammal": {
                "Monkey": 1,
                "Penguin": 0,
                "Platypus": 1,
                "Robin": 0,
                "Turtle": 0
            },
            "Reptile": {
                "Monkey": 0,
                "Penguin": 0,
                "Platypus": 0,
                "Robin": 0,
                "Turtle": 1
            }
        },
        "WarmBlooded": {
            "True": {
                "Bird": 1,
                "Mammal": 1,
                "Reptile": 0
            },
            "False": {
                "Bird": 0,
                "Mammal": 0,
                "Reptile": 1
            }
        },
        "BodyCovering": {
            "Fur": {
                "Bird": 0,
                "Mammal": 1,
                "Reptile": 0
            },
            "Feathers": {
                "Bird": 1,
                "Mammal": 0,
                "Reptile": 0
            },
            "Scales": {
                "Bird": 0,
                "Mammal": 0,
                "Reptile": 1
            }
        }
}