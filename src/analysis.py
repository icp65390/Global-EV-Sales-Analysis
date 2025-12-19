import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ev_sales_2015_2025.csv")

plt.plot(df["Year"], df["EV_Sales_Million"])
plt.title("Global EV Sales Growth (2015–2025)")
plt.xlabel("Year")
plt.ylabel("EV Sales (Million Units)")
plt.grid(True)
plt.show()

