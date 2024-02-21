import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("planetary_k_index_1m.csv")
#data2 = pd.read_csv("dscovr_mag_1s.csv")
print(data.head(2))

# Create a pair plot
sns.pairplot(data, vars = ["time_tag", "kp_index", "estimated_kp"])
plt.show()