from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def run_machine_learning(df):

    print("\n========== MACHINE LEARNING ==========\n")

    encoder = LabelEncoder()

    df["Expansion Recommendation"] = encoder.fit_transform(
        df["Expansion Recommendation"]
    )

    X = df[[
        "EV Population",
        "EV Growth (%)",
        "Charging Sessions",
        "Station Utilization (%)",
        "Queue Length",
        "Coverage Score",
        "Revenue"
    ]]

    y = df["Expansion Recommendation"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    models = {

        "Decision Tree":
        DecisionTreeClassifier(random_state=42),

        "Random Forest":
        RandomForestClassifier(random_state=42),

        "Gradient Boosting":
        GradientBoostingClassifier(random_state=42)

    }

    for name, model in models.items():

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        print("\n", name)

        print("Accuracy :",
              round(accuracy_score(y_test, prediction),4))

        print(classification_report(y_test, prediction))

        if name == "Random Forest":

            print("\nFeature Importance")

            importance = model.feature_importances_

            for feature, score in zip(X.columns, importance):

                print(feature, ":", round(score,4))

        print("-------------------------------------")