from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
students = [
    {"name": "4", "marks": 73}, {"name": "3e7J3kd4L", "marks": 76}, {"name": "iq8l5k", "marks": 79},
    {"name": "Tf3lZ0Wpf", "marks": 71}, {"name": "Hx", "marks": 46}, {"name": "mfuHS", "marks": 26},
    {"name": "FYS", "marks": 11}, {"name": "gVprJ1Mz6", "marks": 73}, {"name": "M", "marks": 7},
    {"name": "he", "marks": 64}, {"name": "9xokztja", "marks": 55}, {"name": "Xg0bxkh", "marks": 37},
    {"name": "fzHE9dpp", "marks": 13}, {"name": "O2wvHv", "marks": 46}, {"name": "B0s5wHR5d", "marks": 80},
    {"name": "yz", "marks": 74}, {"name": "MqnCv", "marks": 80}, {"name": "A", "marks": 96},
    {"name": "llGN", "marks": 67}, {"name": "b", "marks": 96}, {"name": "PsIcKLs", "marks": 32},
    {"name": "CsPx7ww", "marks": 21}, {"name": "5zOWE", "marks": 9}, {"name": "8O0rF", "marks": 12},
    {"name": "MQ3vK", "marks": 1}, {"name": "8iHTc", "marks": 40}, {"name": "kMY4b8HjVS", "marks": 76},
    {"name": "W", "marks": 49}, {"name": "KC4P8WSrjP", "marks": 16}, {"name": "7X", "marks": 70},
    {"name": "klnXcqrB", "marks": 39}, {"name": "ZWUqMUZXS", "marks": 90}, {"name": "4ORJ3LB", "marks": 9},
    {"name": "80vScoLc", "marks": 92}, {"name": "goonzRiOnF", "marks": 64}, {"name": "AOM", "marks": 70},
    {"name": "AkwExBTEm", "marks": 35}, {"name": "RAc", "marks": 1}, {"name": "z", "marks": 21},
    {"name": "ixDfff", "marks": 33}, {"name": "6XT0JocrE", "marks": 41}, {"name": "qPFzI0IJ", "marks": 16},
    {"name": "6Fft", "marks": 84}, {"name": "g6", "marks": 72}, {"name": "2", "marks": 85},
    {"name": "a96u45N", "marks": 2}, {"name": "VJc", "marks": 83}, {"name": "Ympc", "marks": 97},
    {"name": "qVU", "marks": 51}, {"name": "5q", "marks": 59}, {"name": "GpW5uO", "marks": 65},
    {"name": "hs7hdw", "marks": 11}, {"name": "o27", "marks": 75}, {"name": "e5a0IJV", "marks": 13},
    {"name": "kw6", "marks": 23}, {"name": "xjPfZkH1eJ", "marks": 60}, {"name": "fdG3i", "marks": 78},
    {"name": "ULRMw", "marks": 92}, {"name": "l", "marks": 18}, {"name": "5ENA8", "marks": 96},
    {"name": "02e", "marks": 37}, {"name": "tS", "marks": 12}, {"name": "aeehf", "marks": 31},
    {"name": "q", "marks": 66}, {"name": "qRD", "marks": 42}, {"name": "s", "marks": 63},
    {"name": "7hSZej", "marks": 55}, {"name": "u5IiNuFf4", "marks": 74}, {"name": "PWsRN", "marks": 61},
    {"name": "N47u38V6Uh", "marks": 66}, {"name": "NHO2Xrya", "marks": 77}, {"name": "iHNOs", "marks": 82},
    {"name": "vj12g", "marks": 7}, {"name": "kqpk0S", "marks": 71}, {"name": "zEHDeAj75", "marks": 20},
    {"name": "FrpB59P2", "marks": 74}, {"name": "A", "marks": 34}, {"name": "8Rivt", "marks": 84},
    {"name": "azn", "marks": 54}, {"name": "O5NrOVz", "marks": 75}, {"name": "R9gf9x3", "marks": 44},
    {"name": "Gd", "marks": 32}, {"name": "oqB", "marks": 64}, {"name": "idMeG", "marks": 8},
    {"name": "ZWqvnfVKtP", "marks": 73}, {"name": "oiwaKpg", "marks": 86}, {"name": "Tn", "marks": 13},
    {"name": "EC5", "marks": 9}, {"name": "3Yh7", "marks": 67}, {"name": "5xkXSwX", "marks": 42},
    {"name": "Q8", "marks": 23}, {"name": "G3RRcAUDfb", "marks": 48}, {"name": "I1Vra", "marks": 64},
    {"name": "mv2mn", "marks": 79}, {"name": "CHTl", "marks": 70}, {"name": "x", "marks": 63},
    {"name": "ED1jEY", "marks": 10}, {"name": "z4YmlB", "marks": 74}, {"name": "ElHjQpV0Z", "marks": 59},
    {"name": "sc3SB52", "marks": 21}
]

@app.route('/api', methods=['GET'])
def
