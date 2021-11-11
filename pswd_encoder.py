translator = {
    "A": "1",
    "a": "2",
    "b": "3",
    "B": "4",
    "c": "5",
    "C": "6",
    "d": "7",
    "D": "8",
    "E": "9",
    "e": "10",
    "f": "11",
    "F": "12",
    "g": "13",
    "G": "14",
    "h": "15",
    "H": "16",
    "i": "17",
    "I": "18",
    "J": "19",
    "j": "20",
    "k": "21",
    "K": "22",
    "l": "23",
    "L": "24",
    "M": "25",
    "m": "26",
    "N": "27",
    "n": "28",
    "o": "29",
    "O": "30",
    "P": "31",
    "p": "32",
    "q": "33",
    "Q": "34",
    "r": "35",
    "R": "36",
    "S": "37",
    "s": "38",
    "T": "39",
    "t": "40",
    "y": "41",
    "Y": "42",
    "v": "43",
    "V": "44",
    "U": "45",
    "u": "46",
    "z": "47",
    "Z": "48",
    "!": "49",
    "@": "50",
    "#": "51",
    "$": "52",
    "%": "53",
    "^": "54",
    "&": "55",
    "*": "56",
    "(": "57",
    ")": "58",
    "-": "59",
    "_": "60",
    "1": "61",
    "2": "62",
    "3": "63",
    "4": "64",
    "5": "65",
    "6": "66",
    "7": "67",
    "8": "68",
    "9": "69",
    "w": "70",
    "W": "71",
}


def checkpswd(pswd):
    for i in pswd:
        if i in translator.keys():
            continue
        else:
            return False
    return True


def translatepswd(pswd):
    result = []
    for char in pswd:
        result.append(translator.get(char))
    return result
