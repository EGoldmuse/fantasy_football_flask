import pandas as pd
import numpy as np

class Dataloader():

    # https://www.pro-football-reference.com/years/2020/fantasy.htm
    pass_stats = pd.read_csv('pass_data.csv')
    # print(pass_stats.head())

    run_stats = pd.read_csv('rush_data.csv')
    # print(run_stats.head(20))
    # print(run_stats.info())

    rec_stats = pd.read_csv('rec_data.csv')
    # print(rec_stats.head(20))

    def_stats = pd.read_csv('def_data.csv')
    # print(def_stats.head(20))


    dst_stats = pd.read_csv('dst_data.csv')
    # print(dst_stats.head(20))
    # print(dst_stats.tail())
    
    kicker_stats = pd.read_csv('kicker_data.csv')
    # print(kicker_stats.head(20))

    player_run_stats = run_stats['Player']
    # print(player_run_stats)

    fant_o_players = pd.read_csv('fant_o_players.csv')
    print(fant_o_players.head())
    print(fant_o_players.info())

    player_pass_stats = pass_stats['Player']

    player_rec_stats = rec_stats['Player']

    off_players = pd.concat([player_run_stats, player_pass_stats, player_rec_stats])
    off_players = off_players.to_frame()
    off_players = off_players['Player'].drop_duplicates()
    # print(off_players.head())
    # off_player_html = off_players.to_html()
    # print(off_player_html)

