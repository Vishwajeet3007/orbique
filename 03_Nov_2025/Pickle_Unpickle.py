import pickle

# --- Sample data (a Python dictionary) ---
data = {
    "name": "Vishwajeet",
    "age": 23,
    "skills": ["Python", "Machine Learning", "Data Science"]
}

# --- Pickling: Save object to a file ---
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
print("Data has been pickled (saved to data.pkl).")

# --- Unpickling: Load object back from file ---
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
print("Data has been unpickled (loaded from data.pkl).")

# --- Verify the result ---
print("Loaded data:", loaded_data)
