import sqlite3
import pandas as pd
import streamlit as st
import colorama
from colorama import Fore




st.set_page_config(page_title='Player Profile',layout='wide')

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)



#Database connection
db= sqlite3.connect("tennis.sqlite")
cur = db.cursor()

# creating dropbox for players
player_df = pd.read_sql_query("select DISTINCT winner_name from kagglematches ",db)
players=[]
for i in player_df['winner_name']:
    players.append(i)

option = st.selectbox(
    'Select a player',
    (players))    


#total titles
df = pd.read_sql_query(f"select * from kagglematches where winner_name = '{option}' and round='F'", db)
total_titles=len(df['tourney_name'])

# total wins
df = pd.read_sql_query(f"select * from kagglematches where winner_name = '{option}' and round='F'", db)
sqlite_select_query = f"select count(winner_name) from kagglematches where winner_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()
for i in records[0]:
    total_wins=i

# total losses
sqlite_select_query = f"select count(loser_name) from kagglematches where loser_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()
for i in records[0]:
    total_loss=i

# win percent
win_percent = (total_wins/(total_wins+total_loss))*100

#HARD COURT
 #wins
sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Hard' and winner_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()

for i in records[0]:
    hard_wins=i

 #losses
sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Hard' and loser_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()

for i in records[0]:
    hard_losses=i


#GRASS COURT
 #wins
sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Grass' and winner_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()

for i in records[0]:
    grass_wins=i


 #losses
sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Grass' and loser_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()

for i in records[0]:
    grass_losses=i

#CLAY COURT
 #wins
sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Clay' and winner_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()

for i in records[0]:
    clay_wins=i

 #losses
sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Clay' and loser_name = '{option}'"
cur.execute(sqlite_select_query)
records = cur.fetchall()

for i in records[0]:
    clay_losses=i


st.title(f"{option}")
st.write("---------------")
st.write("")
def load_data():
    return pd.DataFrame(
        {
            " ": ["Total Career Ttitle", "Total Career Wins","Total Career loss" ,"Total Career win percent",'Number of grand slams won',"country","best on"],
            "": [total_titles, total_wins, total_loss, win_percent,"Test","test","test"],
        }
    )
df = load_data()

import matplotlib.pyplot as plt
import seaborn
from io import BytesIO
  
# plotting a pie chart
data = [total_wins, total_loss]
keys = ['Wins', 'Losses']
  

explode = [0.1, 0]

palette_color = seaborn.color_palette('dark')

fig = plt.figure(figsize=(2.5,2.5)) 
ax = plt.axes()

plt.title(f"out of total {total_wins+total_loss} macthes played")

ax.pie(data, labels=keys, colors=palette_color,
        explode=explode, autopct='%.0f%%')


  
# displaying chart

with st.container():
    left_column,middle_column,right_columns = st.columns(3)
    with middle_column:
        st.subheader("⠀⠀Highlights")
        st.subheader("")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(f'<p class="big-font"> GRAND SLAMS⠀⠀⠀⠀⠀⠀⠀ </p>', unsafe_allow_html=True)
        st.write("--------------------------------------")
        st.markdown(f'<p class="big-font">Total Ti‎‎tles⠀⠀⠀⠀⠀⠀⠀{total_titles} </p>', unsafe_allow_html=True)
        st.write("--------------------------------------")
        st.markdown(f'<p class="big-font">Total Wins⠀⠀⠀⠀⠀⠀⠀{total_wins} </p>', unsafe_allow_html=True)
        st.write("--------------------------------------")
        st.markdown(f'<p class="big-font">Total Career Loss⠀⠀⠀{total_loss} </p>', unsafe_allow_html=True)
        st.write("--------------------------------------")
        st.markdown(f'<p class="big-font">Win Percentage⠀⠀⠀⠀{round(win_percent)}%</p>', unsafe_allow_html=True)
        st.write("--------------------------------------")
    with right_column:
        st.pyplot(fig)









# plotting a pie chart
data = [hard_wins, clay_wins, grass_wins]
keys = ['Hard Court', 'Grass Court','Clay Court']
  

explode = [0, 0,0]

palette_color = seaborn.color_palette('dark')



fig = plt.figure(figsize=(3,3))

ax = plt.axes()
plt.title(f"share of each surface out of total wins")
ax.pie(data, labels=keys, colors=palette_color,
        explode=explode, autopct='%.0f%%')






with st.container():
    left_column,middle_column,right_column = st.columns(3)
    with middle_column:
        st.write("")
        st.write("")
        st.subheader("Surface wise performace")


        

with st.container():
    left_column,middle_column,right_column = st.columns(3)
    with left_column:
        st.write("----------")
        st.markdown(f'<p class="big-font">HARD COURTS</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font">Wins⠀⠀⠀{hard_wins}</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font"> Losses⠀⠀{hard_losses}</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font">Win % ⠀⠀{round((hard_wins/(hard_losses+hard_wins))*100)}%</p>', unsafe_allow_html=True)
        st.write("----------")

    with middle_column:
        st.write("----------")
        st.markdown(f'<p class="big-font">GRASS COURTS</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font">Wins⠀⠀⠀{grass_wins}</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font"> Losses⠀⠀{grass_losses}</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font">Win % ⠀⠀{round((grass_wins/(grass_losses+grass_wins))*100)}%</p>', unsafe_allow_html=True)
        st.write("----------")

    with right_column:
        st.write("----------")
        st.markdown(f'<p class="big-font">CLAY COURTS</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font">Wins⠀⠀⠀{clay_wins}</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font"> Losses⠀⠀{clay_losses}</p>', unsafe_allow_html=True)
        st.write("----------")
        st.markdown(f'<p class="big-font">Win % ⠀⠀{round((clay_wins/(clay_losses+clay_wins))*100)}%</p>', unsafe_allow_html=True)
        st.write("----------")
    





st.write(" ")

#with st.container():
#    #st.write("Hard Court Performance :-")
#    def load_data():
#        return pd.DataFrame(
#            {
#                "Surface":["Hard court", "Grass Court","Clay Court"],
#               "Wins": [hard_wins, grass_wins, clay_wins],
#                "Losses" :[hard_losses,grass_losses,clay_losses],
#                "Win %" : [(hard_wins/(hard_losses+hard_wins))*100,(grass_wins/(grass_losses+grass_wins))*100,(clay_wins/(clay_losses+clay_wins))*100],
#            }
#        )
#    df = load_data()
#    st.dataframe(df,use_container_width=True)
#st.write("  ")




import streamlit as st
import pandas as pd
import numpy as np

arr =[[ 'wins','Loses']]

chart_data = pd.DataFrame({
    'index': ['Wins', 'Losses'],
    'sports_teams': [hard_wins, hard_losses]
}).set_index('index')


#columns=["Wins", "Losses"])
#arr =[[ hard_wins,  hard_losses],
#       [ grass_wins,  grass_losses],
#       [clay_wins, clay_losses]]

#chart_data = pd.DataFrame(
#    arr,
#    columns=[hard_wins,  hard_losses])



#with st.container():
#    left_column, right_column = st.columns(2)
#    with left_column:
#        #st.bar_chart(chart_data,height=5)
#        st.write("First Bar Represents HARD COURT")
#        st.write("Second Bar Represents GRASS COURT")
#        st.write("Third Bar Represents CLAY COURT")
        
#    with right_column:
#        st.pyplot(fig)


x = ['A', 'B', 'C', 'D']
y1 = [10, 20, 10, 30]
y2 = [20, 25, 15, 25]
 








with st.container():
    left_column,middle_column,right_column = st.columns(3)
    with middle_column:
        st.pyplot(fig)


