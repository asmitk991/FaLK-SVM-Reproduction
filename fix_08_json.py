import json

nb_path = "notebooks/08_Failure_Modes.ipynb"
with open(nb_path, "r") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        new_source = []
        i = 0
        while i < len(source):
            line = source[i]
            if "plt.bar(['Global Linear SVM\\\\n" in line or "plt.bar(['Global Linear SVM\\n" in line:
                # Concatenate the next 3 lines
                if i + 3 < len(source):
                    full_line = source[i].replace("\\n", "\\n(3000 features)', 'FaLK-SVM\\n(50 features)', 'FaLK-SVM\\n(3000 features)'], \\n")
                    full_line += source[i+4] if i+4 < len(source) and "color=['blue'" in source[i+4] else ""
                    
                    # We only want to insert the fixed version for plt.bar(...)
                    fixed = "plt.bar(['Global Linear SVM\\n(3000 features)', 'FaLK-SVM\\n(50 features)', 'FaLK-SVM\\n(3000 features)'], \\n        [acc_lin*100, acc_md*100, acc_falk*100], color=['blue', 'green', 'gray'])\\n"
                    new_source.append(fixed)
                    i += 4
                    continue
            new_source.append(line)
            i += 1
            
        cell["source"] = new_source

with open(nb_path, "w") as f:
    json.dump(nb, f, indent=1)

print("08 notebook fixed.")
