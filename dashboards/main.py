import pandas as pd
from ev_analysis import analyze_data
from ml_model import run_machine_learning

def main():

    print("========================================")
    print(" EV CHARGING NETWORK PLANNER ")
    print("========================================")

    df = pd.read_csv(r"C:\Users\tamba\Downloads\Viniksha\Task3\ev1.csv")

    analyze_data(df)

    run_machine_learning(df)

    print("\nProject Completed Successfully.")

if __name__ == "__main__":
    main()