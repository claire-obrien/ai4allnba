import json
import pandas as pd
import gzip
from bs4 import BeautifulSoup


# load the profiles database and produce a table keyed on player/year?
def load_profiles(file_name="player_profiles.json"):
    opener = gzip.open if file_name.endswith(".gz") else open
    with opener(file_name, "r") as f:
        js = json.load(f)
    result_sets = js["resultSets"][0]
    headers = result_sets["headers"]
    data_rows = result_sets["rowSet"]

    data_dict = {
        header : [ 
            data_row[ctr]
            for data_row in data_rows
        ]
        for ctr, header in enumerate(headers)
    }

    df = pd.DataFrame(data_dict)
    return df


# load the injury data for each file
def load_injury_data(file_name: str):
def load_injury_data(file_name: str):
    # these are the columns we expect, in the order we expect them
    expected_columns = ["Player","Position","Updated","Injury","Injury Status"]
    
    # these are the columns whose names need to be rewritten old->new
    rewrite_columns = { "Expected Return": "Injury Status", "Pos": "Position" }
    
    with open(file_name) as fp:
        html_data = BeautifulSoup(fp, 'html.parser')
    # construct the header
    first_table = (html_data.find("table", {"class": "TableBase-table"}) or
            html_data.find("table", {"class": "data"}))
    header = [
        th.text.strip()
        for th in (
            (first_table.find_all("th", {"class": "TableBase-headTh"}) or 
            first_table.find("tr", {"id": "special"}).find_all("td"))
        )
    ]
    # construct the data
    injuries = {
        hdr: []
        for hdr in expected_columns
    }
    tables = (html_data.find_all("table", {"class": "TableBase-table"}) or
            html_data.find_all("table", {"class": "data"}))
    for table in tables:
        # this is broken for years before 2017
        for row in table.find_all("tr"):
            if (not ("bodyTr" in row.attrs["class"][0] or "row" in row.attrs["class"][0])) or ("id" in row.attrs):
                continue
            # TODO: you need to special handle the Player name field (first one)
            # there is a span called "CellPlayerName--long" that needs to be extracted
            cells = [
                (cell.find("span", {"class": "CellPlayerName--long"}) or cell).text.strip() 
                for ctr, cell in enumerate(
                row.find_all("td")
                )
            ]
            if len(cells) < len(header):
                continue
            for ctr, hdr in enumerate(header):
                injuries[rewrite_columns.get(hdr, hdr)].append(cells[ctr])
    df = pd.DataFrame(injuries)
    return df


# EF: to get all injury data, you need the data from every year
def load_injury_data_from_all_years(base_name: str = "nbainjuries.html",
                                    start_year: int = 2012, end_year: int = 2021):
    all_year_data = []
    for year in range(start_year, end_year+1):
        year_file_name = f"{year}{base_name}"
        print(f"trying {year_file_name}")
        all_year_data.append(load_injury_data(year_file_name))
    return pd.concat(all_year_data)

# join the profile data to the injury data
#join in pandas, all year data + injury data, joining what I think
#they are stored in
df.join(load_injury_data, all_year_data)
# get player stats for a season:

# union it together - injury_data- 
# join the injury data to the game data
#every player-game, we have it, join key, join it together
# EF: you need to actually load the data!
season_data = load_profiles("season_data.json.gz")
#build functions for each SeasonType
#CONFUSION- Co
# season_data includes all player-game combinations from all seasons
print(season_data)



#player_profiles
# get a list of player+game
print(player_profiles)
#printing where I think this is stored- CO
# convert all features to numerics
json.parse(player_profiles)
# add derived features / corrections 
# player profile age - current; age at the time of the game is what you need.
age= df[df["AGE"]]
# df: player-game, features..., label
df= pd[player-game]
# split into train/test set that are relatively independent
#model
X= df[player-game]
Y= season_data
# set up an ML algorithm (decision tree, random forest)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# play with the hyperparameters (or use tuning)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
# test on the test set, iterate
y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)
from sklearn.metrics import mean_squared_error, r2_score
lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)
lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)
print(lr_train_mse)
# save the model 
#used this for code: https://towardsdatascience.com/how-to-build-your-first-machine-learning-model-in-python-e70fd1907cdd


# find the model metrics with respect to the test set (f1, precision, recall, area under roc, etc) 

# when you get a "reasonable" model, stop and make graphs...
