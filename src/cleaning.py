import pandas as pd
import numpy as np


def clean_sex(column):
    column=column.str.extract("(^M|F)")
    return column



def clean_fatality(column):
    column = column.str.extract("(^Y|N)")
    return column

def extract_age(column):
    column = column.str.extract("(\d{1,2})")
    return column

def clean_species(column):
    column = column.str.extract("([A-Z|a-z]{1,}\s{1}shark)")
    return column

def clean_activities(column):
    new_activity = []
    # I will group activities within the following groups ["Diving", "Surfing", "Swimming", "Fishing","Walking", "Sailing","Other"]
    column=column.str.upper()
    activity= column

    for word in activity:
        word=str(word)
        if "SURF" in word:
            new_activity.append("Surfing")
        
        elif "SURFING" in word:
            new_activity.append("Surfing")
        
        elif "PADDL" in word:
            new_activity.append("Surfing")

        elif "DIVE" in word:
            new_activity.append("Diving")
        
        elif "DIVING" in word:
            new_activity.append("Diving")

        elif "SWIM" in word:
            new_activity.append("Swimming")
        
        elif "FLOAT" in word:
            new_activity.append("Swimming")
        
        elif "FISH" in word:
            new_activity.append("Fishing")
        
        elif "NETS" in word:
            new_activity.append("Fishing")

        elif "WALK" in word:
            new_activity.append("Walking")

        elif "BOAT" in word:
            new_activity.append("Sailing")

        else:
            new_activity.append("Other")
    return new_activity
            

def create_season (hemis,month):
    season_list = []
    list_hemis = list(hemis)
    list_month = list(month)

    for h,m in zip(list_hemis,list_month):
        if h == "NORTH":
            if m in range(1,4):
                season_list.append("WINTER")
            elif m in range(4,7):
                season_list.append("SPRING")
            elif m in range(7,10):
                season_list.append("SUMMER")
            elif m in range(10,13):
                season_list.append("AUTUMN")
            else: 
                season_list.append("NOT DEFINED")

        elif h == "SOUTH":
            if m in range(1,4):
                season_list.append("SUMMER")
            elif m in range(4,7):
                season_list.append("AUTUMN")
            elif m in range(7,10):
                season_list.append("WINTER")
            elif m in range(10,13):
                season_list.append("SPRING")
            else: 
                season_list.append("NOT DEFINED")
    return season_list

def get_hemisphere(column):
    south = pd.read_csv ('./data/south.csv', encoding='unicode_escape')
    # column name --> ï»¿SOUTH COUNTRY 

    list_south = []
    for elem in south["ï»¿SOUTH COUNTRY"]:
        list_south.append(elem)
    
    newcolumn = np.where(column.isin(list_south), 'SOUTH', 'NORTH')
    return newcolumn