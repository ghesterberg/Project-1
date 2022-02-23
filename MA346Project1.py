import pandas as pd

dfPresident = pd.read_csv("C:\\Users\\grace\\OneDrive\\Documents\\GitHub\\Project-1\\us_pres_election.csv")
dfVaccination = pd.read_csv("C:\\Users\\grace\\OneDrive\\Documents\\GitHub\\Project-1\\us_state_vaccinations.csv")

def getStateInfo(state, columnName):

    dfState = dfVaccination[dfVaccination["location"] == state].set_index('date')

    print(dfState[columnName])

getStateInfo("Idaho", "total_vaccinations_per_hundred")
