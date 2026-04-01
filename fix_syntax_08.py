import os

nb_path = "notebooks/08_Failure_Modes.ipynb"
with open(nb_path, "r") as f:
    text = f.read()

# Replace multiple split lists conceptually into one single valid line representation
text = text.replace('"plt.bar([\\'Global Linear SVM\\\\n",\n    "(3000 features)\\', \\'FaLK-SVM\\\\n",\n    "(50 features)\\', \\'FaLK-SVM\\\\n",\n    "(3000 features)\\'], \\n        [acc_lin*100, acc_md*100, acc_falk*100], color=[\\'blue\\', \\'green\\', \\'gray\\'])\\nplt.ylabel(\\'Test Accuracy (%)\\')\\nplt.title(\\'Failure Mode Degradation Curve\\')\\nplt.savefig(\\"results/task_3_2_failure_mode.png\\")\\nplt.show()\\n"', '"plt.bar([\\'Global Linear SVM\\\\n(3000 features)\\', \\'FaLK-SVM\\\\n(50 features)\\', \\'FaLK-SVM\\\\n(3000 features)\\'], \\n        [acc_lin*100, acc_md*100, acc_falk*100], color=[\\'blue\\', \\'green\\', \\'gray\\'])\\nplt.ylabel(\\'Test Accuracy (%)\\')\\nplt.title(\\'Failure Mode Degradation Curve\\')\\nplt.savefig(\\"results/task_3_2_failure_mode.png\\")\\nplt.show()\\n"')

with open(nb_path, "w") as f:
    f.write(text)

print("08 replaced.")
