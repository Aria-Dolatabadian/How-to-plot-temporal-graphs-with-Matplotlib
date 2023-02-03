import pandas as pd
df = pd.read_csv (r'temporal.csv')
print (df)
format_dict = {'Australia':'${0:,.2f}', 'Mes':'{:%m-%Y}', 'Europe':'{:.2%}'}
#We make sure that the Month column has date time format
df['Mes'] = pd.to_datetime(df['Mes'])
#We apply the style to the visualization
df.head().style.format(format_dict)
import matplotlib.pyplot as plt
plt.plot(df['Mes'], df['Australia'], label='Australia')
plt.plot(df['Mes'], df['Europe'], label='Europe')
plt.plot(df['Mes'], df['Africa'], label='Africa')
plt.xlabel('Date')
plt.ylabel('Percentage')
plt.title('Production since 2004')
plt.grid(True)
plt.legend()
plt.show()
fig, axes = plt.subplots(2,2)
axes[0, 0].hist(df['Australia'])
axes[0, 1].scatter(df['Mes'], df['Australia'])
axes[1, 0].plot(df['Mes'], df['Europe'])
axes[1, 1].plot(df['Mes'], df['Africa'])
plt.show()
# We can draw the graph with different styles for the points of each variable:
plt.plot(df['Mes'], df['Australia'], 'r-')
plt.plot(df['Mes'], df['Australia']*2, 'bs')
plt.plot(df['Mes'], df['Australia']*3, 'g^')
plt.show()
# scatterplot
plt.scatter(df['Australia'], df['Europe'])
plt.show()
# bar chart
plt.bar(df['Mes'], df['Europe'], width=20)
plt.show()
# histogram
plt.hist(df['Africa'], bins=15)
plt.show()
