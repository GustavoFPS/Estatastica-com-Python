
fig, ax = plt.subplots()
box = ax.boxplot(data_boxplot, patch_artist=True, showfliers=False)
plt.show()