netwrok = "animal"

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
            "Animal.Monkey": 0,
            "Animal.Penguin": 0,
            "Animal.Platypus": 0,
            "Animal.Robin": 0.5,
            "Animal.Turtle": 0
        },
        "Land": {
            "Animal.Monkey": 1,
            "Animal.Penguin": 0.5,
            "Animal.Platypus": 0,
            "Animal.Robin": 0.5,
            "Animal.Turtle": 0.5
        },
        "Water": {
            "Animal.Monkey": 0,
            "Animal.Penguin": 0.5,
            "Animal.Platypus": 1,
            "Animal.Robin": 0,
            "Animal.Turtle": 0.5
        }
    },
    "HasShell": {
        "True": {
            "Animal.Monkey": 0,
            "Animal.Penguin": 0,
            "Animal.Platypus": 0,
            "Animal.Robin": 0,
            "Animal.Turtle": 1
        },
        "False": {
            "Animal.Monkey": 1,
            "Animal.Penguin": 1,
            "Animal.Platypus": 1,
            "Animal.Robin": 1,
            "Animal.Turtle": 0
        }
    },
    "BearsYoungAs": {
        "Live": {
            "Animal.Monkey": 1,
            "Animal.Penguin": 0,
            "Animal.Platypus": 0,
            "Animal.Robin": 0,
            "Animal.Turtle": 0
        },
        "Eggs": {
            "Animal.Monkey": 0,
            "Animal.Penguin": 1,
            "Animal.Platypus": 1,
            "Animal.Robin": 1,
            "Animal.Turtle": 1
        }
    },
    "Class": {
        "Bird": {
            "Animal.Monkey": 0,
            "Animal.Penguin": 1,
            "Animal.Platypus": 0,
            "Animal.Robin": 1,
            "Animal.Turtle": 0
        },
        "Mammal": {
            "Animal.Monkey": 1,
            "Animal.Penguin": 0,
            "Animal.Platypus": 1,
            "Animal.Robin": 0,
            "Animal.Turtle": 0
        },
        "Reptile": {
            "Animal.Monkey": 0,
            "Animal.Penguin": 0,
            "Animal.Platypus": 0,
            "Animal.Robin": 0,
            "Animal.Turtle": 1
        }
    },
    "WarmBlooded": {
        "True": {
            "Class.Bird": 1,
            "Class.Mammal": 1,
            "Class.Reptile": 0
        },
        "False": {
            "Class.Bird": 0,
            "Class.Mammal": 0,
            "Class.Reptile": 1
        }
    },
    "BodyCovering": {
        "Fur": {
            "Class.Bird": 0,
            "Class.Mammal": 1,
            "Class.Reptile": 0
        },
        "Feathers": {
            "Class.Bird": 1,
            "Class.Mammal": 0,
            "Class.Reptile": 0
        },
        "Scales": {
            "Class.Bird": 0,
            "Class.Mammal": 0,
            "Class.Reptile": 1
        }
    }
}