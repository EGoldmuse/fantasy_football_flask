from app import app
from flask import jsonify, render_template, request, session, redirect
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
import pandas as pd
import numpy as np
import csv


'''
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
'''

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/draft')
# @login_required
def draft():
    return render_template('draft.html')

@app.route('/players')
def players():
    return render_template('players.html')

@app.route('/team_d')
def team_d():
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
    return render_template("team_d.html", dst=dst)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/rushing")
def run_data():
  with open('./rush_data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    rushers = []
    for row in data:
      if not first_line:
        rushers.append({
          "Rk": row[0],
          "Player": row[1],
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
          "Fmb": row[14]
        })
      else:
        first_line = False
  return render_template("rushers.html", rushers=rushers)    

@app.route("/passing")
def pass_data():
  with open('./pass_data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    passers = []
    for row in data:
      if not first_line:
        passers.append({
          "Rk": row[0],
          "Player": row[1],
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
          "YG": row[21],
          "Rate": row[22],
          "QBR": row[23],
          "Sk": row[24],
          "YdsLost": row[25],
          "NYA": row[26],
          "ANYA": row[27],
          "Sk%": row[28],
          "FourthQC": row[29],
          "GWD": row[30]
        })
      else:
        first_line = False
  return render_template("passers.html", passers=passers) 

@app.route('/receivers')
def rec_data():
    with open('./rec_data.csv') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        first_line = True
        receivers = []
        for row in data:
            if not first_line:
                receivers.append({
                "Rk": row[0],
                "Player":row[1],
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
    return render_template("receivers.html", receivers=receivers) 

@app.route('/playerdata')
def html_table():
    return render_template('player_html')
