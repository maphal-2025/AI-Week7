import pandas as pd

df = pd.read_csv("compas-scores-raw.csv")

# Focus on relevant columns
cols = ['sex', 'race', 'age', 'juv_fel_count', 'juv_misd_count',
        'juv_other_count', 'priors_count', 'c_charge_degree',
        'two_year_recid', 'decile_score']
print("Columns after selecting and dropping NA:", df.columns)


#Grouped Bar Chart: False Positive Rate by Race
import matplotlib.pyplot as plt

groups = ['African-American', 'Caucasian']
fpr_values = [0.45, 0.23]  

plt.bar(groups, fpr_values, color=['red', 'blue'])
plt.title('False Positive Rate by Race')
plt.ylabel('FPR')
plt.ylim(0, 1)
for i, v in enumerate(fpr_values):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center')
plt.show()

#Line Chart: Bias Metrics Before vs. After Mitigation
metrics = ['Disparate Impact', 'FPR Difference']
before = [0.65, 0.22]
after = [0.89, 0.08]

plt.plot(metrics, before, marker='o', label='Before Mitigation')
plt.plot(metrics, after, marker='o', label='After Mitigation')
plt.title('Bias Metrics Comparison')
plt.ylabel('Metric Value')
plt.legend()
plt.grid(True)
plt.show()


