from .import bp as api
from flask import jsonify, request
import csv
import re

# api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/rushers')
def rushdata():
        # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)

    with open('./rush_data.csv') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        first_line = True
        rushers = []
        for row in data:
            if not first_line:
                rushers.append({
                "Rk": row[0],
                "Player": re.split(r"[*|\\]", row[1])[0].strip(),
                "Tm": row[2],
                "Age": row[3],
                "Pos": row[4],
                "G": row[5],
                "GS": row[6],
                "RuAtt": row[7],
                "RuYds": row[8],
                "RuTD": row[9],
                "Ru1D": row[10],
                "RuLng": row[11],
                "RuYA": row[12],
                "RuYG": row[13],
                "FMB": row[14]
                })
            else:
                first_line = False
        # response
    return {
        'data': rushers,
        # 'recordsFiltered': len(data),
        # 'recordsTotal': len(data),
        # 'draw': request.args.get('draw', type=int),
    }

@api.route('/passers')
def passdata():
        # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)

    with open('./pass_data.csv') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        first_line = True
        passers = []
        for row in data:
            if not first_line:
                passers.append({
                "Rk": row[0],
                "Player": re.split(r"[*|\\]", row[1])[0].strip(),
                "Tm": row[2],
                "Age": row[3],
                "Pos": row[4],
                "G": row[5],
                "GS": row[6],
                "QBrec": row[7],
                "Cmp": row[8],
                "Att": row[9],
                "Cmp%": row[10],
                "Yds": row[11],
                "TD": row[12],
                "TD%": row[13],
                "Int": row[14],
                "Int%": row[15],
                "FirstD": row[16],
                "Lng": row[17],
                "YA": row[18],
                "AYA": row[19],
                "YC": row[20],
                "Rate": row[21],
                "QBR": row[22],
                "Sk": row[23],
                "YdsLost": row[24],
                "NYA": row[25],
                "ANYA": row[26],
                "Sk%": row[27],
                "FourthQC": row[28],
                "GWD": row[29]
                })
            else:
                first_line = False
        # response
    return {
        'data': passers,
        # 'recordsFiltered': len(data),
        # 'recordsTotal': len(data),
        # 'draw': request.args.get('draw', type=int),
    }

@api.route('/receivers')
def recdata():
        # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)

    with open('./rec_data.csv') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        first_line = True
        receivers = []
        for row in data:
            if not first_line:
                receivers.append({
                "Rk": row[0],
                "Player": re.split(r"[*|\\]", row[1])[0].strip(),
                "Tm": row[2],
                "Age": row[3],
                "Pos": row[4],
                "G": row[5],
                "GS": row[6],
                "Tgt": row[7],
                "Rec": row[8],
                "Ctch%": row[9],
                "Yds": row[10],
                "YR": row[11],
                "TD": row[12],
                "FirstD": row[13],
                "Lng": row[14],
                "YTgt": row[15],
                "RPG": row[16],
                "YPG": row[17],
                "FMB": row[18]
                })
            else:
                first_line = False
        # response
    return {
        'data': receivers,
        # 'recordsFiltered': len(data),
        # 'recordsTotal': len(data),
        # 'draw': request.args.get('draw', type=int),
        }

@api.route('/team_d')
def teamd():

    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)

    with open('./dst_updated.csv') as csv_file:
      data = csv.reader(csv_file, delimiter=',')
      first_line = True
      dst = []
      for row in data:
        if not first_line:
          dst.append({
            "Rk": row[0],
            "Player": row[1],
            "Tm": row[2],
            "G": row[3],
            "PF": row[4],
            "Yds": row[5],
            "Ply": row[6],
            "Y/P": row[7],
            "TO": row[8],
            "Int": row[9],
            "Sc%": row[10],
            "TO%": row[11]
          })
        else:
          first_line = False
    return {
        'data': dst,
        }