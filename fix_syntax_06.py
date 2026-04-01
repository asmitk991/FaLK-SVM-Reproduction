import os

nb_path = "notebooks/06_Results_and_Validation.ipynb"
with open(nb_path, "r") as f:
    text = f.read()

text = text.replace('"print(f\\"\\\\n)\\n",\\n     "Mean Accuracy: {mean_acc:.2f}% ± {std_acc:.2f}%\\")\\n"', '"print(f\\"\\\\nMean Accuracy: {mean_acc:.2f}% ± {std_acc:.2f}%\\")\\n"')

with open(nb_path, "w") as f:
    f.write(text)

print("06 replaced.")
