import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("career_data.csv")

# Split features and target
X = data.drop("Career", axis=1)
y = data["Career"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Take student input
print("Enter your skill levels (1 to 10):")
math = int(input("Math Skills: "))
programming = int(input("Programming Skills: "))
creativity = int(input("Creativity: "))
communication = int(input("Communication Skills: "))
marks = int(input("Marks (%): "))

# Create DataFrame for prediction
input_data = pd.DataFrame(
    [[math, programming, creativity, communication, marks]],
    columns=["Math", "Programming", "Creativity", "Communication", "Marks"]
)

# Predict career
prediction = model.predict(input_data)

print("\n✅ Recommended Career:", prediction[0])
