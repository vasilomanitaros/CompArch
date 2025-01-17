import matplotlib.pyplot as plt

# X-axis values
x_values = [2,4,8,16]

# Y-axis values for each benchmark
specbzip = [5.284838, 5.283085, 5.495165, 5.025019]
spechmmer = [1.657753, 1.567920, 1.515549, 1.486987]
speclibm = [3.896239, 2.551809, 1.963812, 1.647739]
specmcf = [1.468958, 1.349799, 1.270171, 1.223331]
specsjeng = [1.271758, 1.220581, 1.194251, 1.180894]

# Plotting the values
plt.figure(figsize=(10, 6))
plt.plot(x_values, specbzip, marker='o', linestyle='-', label='specbzip')
plt.plot(x_values, spechmmer, marker='o', linestyle='-', label='spechmmer')
plt.plot(x_values, speclibm, marker='o', linestyle='-', label='speclibm')
plt.plot(x_values, specmcf, marker='o', linestyle='-', label='specmcf')
plt.plot(x_values, specsjeng, marker='o', linestyle='-', label='specsjeng')


plt.title('CPI vs. L2 Associativity')
plt.xlabel(' L2 Associativity')
plt.ylabel('CPI')
plt.grid(True)
plt.legend()
plt.xticks(x_values)
plt.tight_layout()
plt.savefig('cpi_vs_l2assoc.png')
plt.show()

# l1
# specbzip = [5.284838, 5.285654, 5.285654]
# spechmmer = [1.568465, 1.567920, 1.567920]
# speclibm = [2.551809, 2.551809, 2.551809]
# specmcf = [1.349799, 1.349799, 1.349799]
# cls
# specbzip = [9.757687, 5.285654, 5.495165, 5.020159]
# spechmmer = [1.657753, 1.567920, 1.515549, 1.486987]
# speclibm = [3.896239, 2.551809, 1.963812, 1.647739]
# specmcf = [1.468958, 1.349799, 1.270171, 1.223331]
# l1datassoc
# specbzip = [5.285654, 5.285654, 5.495165, 5.020159]
# spechmmer = [1.657753, 1.567920, 1.515549, 1.486987]
# speclibm = [3.896239, 2.551809, 1.963812, 1.647739]
# specmcf = [1.468958, 1.349799, 1.270171, 1.223331]
# specsjeng = [1.271758, 1.220581, 1.194251, 1.180894]
# l2
# specbzip = [5.332177, 5.285654, 5.458677]
# spechmmer = [1.657753, 1.567920, 1.515549]
# speclibm = [3.896239, 2.551809, 1.963812]
# specmcf = [1.468958, 1.349799, 1.270171]
# specsjeng = [1.271758, 1.220581, 1.194251]
# l2assoc
# specbzip = [5.284838, 5.283085, 5.495165, 5.025019]
# spechmmer = [1.657753, 1.567920, 1.515549, 1.486987]
# speclibm = [3.896239, 2.551809, 1.963812, 1.647739]
# specmcf = [1.468958, 1.349799, 1.270171, 1.223331]
# specsjeng = [1.271758, 1.220581, 1.194251, 1.180894]