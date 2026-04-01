import json

# Fix 04_Data_Generation.ipynb
nb_path = "notebooks/04_Data_Generation.ipynb"
with open(nb_path, "r") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        new_source = []
        for line in source:
            if line == "\\\\n\\n":
                new_source.append("\\n")
            elif line.startswith("print(f\\\\\\\"Class"):
                new_source.append(line.replace("\\\\\\\"", "\\\""))
            else:
                new_source.append(line)
        cell["source"] = new_source

with open(nb_path, "w") as f:
    json.dump(nb, f, indent=1)

print("Fixed syntax error in notebook 04.")
