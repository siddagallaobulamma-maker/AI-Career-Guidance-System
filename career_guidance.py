import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("career_data.csv")
X = data.drop("Career", axis=1)
y = data["Career"]
model = DecisionTreeClassifier()
model.fit(X, y)
print("Enter your skill levels (1 to 10):")
math = int(input("Math Skills: "))
programming = int(input("Programming Skills: "))
creativity = int(input("Creativity: "))
communication = int(input("Communication Skills: "))
marks = int(input("Marks (%): "))
input_data = pd.DataFrame(
    [[math, programming, creativity, communication, marks]],
    columns=["Math", "Programming", "Creativity", "Communication", "Marks"]
)
prediction = model.predict(input_data)

print("\n✅ Recommended Career:", prediction[0])
