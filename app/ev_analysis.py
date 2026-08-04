import pandas as pd

def analyze_data(df):

    print("\n========== DATA ANALYSIS ==========\n")

    print("Total Stations :", df["Station ID"].nunique())

    print("Total EV Population :", df["EV Population"].sum())

    print("Average Station Utilization :",
          round(df["Station Utilization (%)"].mean(),2))

    print("Average Queue Length :",
          round(df["Queue Length"].mean(),2))

    print("Average Charging Time :",
          round(df["Average Charging Time (min)"].mean(),2))

    print("Total Revenue :",
          round(df["Revenue"].sum(),2))

    print("\nStations by City")

    print(df["City"].value_counts())

    print("\nCharger Types")

    print(df["Charger Type"].value_counts())

    print("\nExpansion Recommendation")

    print(df["Expansion Recommendation"].value_counts())

    print("\nTop Expansion Priority Locations")

    print(
        df.sort_values(
            "Expansion Priority Index",
            ascending=False
        )[[
            "City",
            "Station ID",
            "Expansion Recommendation",
            "Expansion Priority Index"
        ]].head(10)
    )