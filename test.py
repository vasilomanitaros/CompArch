# import matplotlib.pyplot as plt

# # Costs for each combination
# costs = [72.4, 82.8, 116.4, 89.6, 109.6, 124.8, 146.4, 140.8, 163.2, 158.4, 188.8, 189.6, 200]

# # Values for each combination
# values = [1.154747, 1.140655, 1.154434, 1.114332, 1.139768, 1.137877, 1.138424, 1.138344, 1.100838, 1.137877, 1.137876, 1.111727, 1.099413]


# # Plotting the values
# plt.figure(figsize=(10, 6))
# plt.scatter(costs, values, color='b')
# plt.title('CPI vs. Costs')
# plt.xlabel('Cost')
# plt.ylabel('Benchmark Value')
# plt.grid(True)
# plt.xticks(costs, rotation=45)
# plt.tight_layout()
# plt.savefig('mcf_vs_costs.png')
# plt.show()

# #bzip
# #values = [1.741476, 1.612662, 1.721366, 1.603746, 1.591759, 1.574462, 1.580758, 1.588863, 1.589487, 1.574462, 1.566864, 1.574459, 1.540347]
# #hmmer
# #values = [1.191861, 1.184813, 1.191673, 1.179548, 1.182888, 1.182888, 1.184853, 1.184782, 1.177232, 1.182888, 1.182435, 1.179539, 1.176000]
# #libm
# #values = [3.922231, 2.624355, 3.922235, 1.991078, 2.624355, 2.623265, 2.620761, 2.623265, 1.654701, 2.623265, 2.623265, 1.989118, 1.653858]
# #mcf
# #values = [1.154747, 1.140655, 1.154434, 1.114332, 1.139768, 1.137877, 1.138424, 1.138344, 1.100838, 1.137877, 1.137876, 1.111727, 1.099413]

import matplotlib.pyplot as plt

# Costs for each combination
costs = [72.4, 82.8, 116.4, 89.6, 109.6, 124.8, 146.4, 140.8, 163.2, 158.4, 188.8, 189.6, 200]

# Values for each benchmark
bzip_values = [1.741476, 1.612662, 1.721366, 1.603746, 1.591759, 1.574462, 1.580758, 1.588863, 1.589487, 1.574462, 1.566864, 1.574459, 1.540347]
hmmer_values = [1.191861, 1.184813, 1.191673, 1.179548, 1.182888, 1.182888, 1.184853, 1.184782, 1.177232, 1.182888, 1.182435, 1.179539, 1.176000]
libm_values = [3.922231, 2.624355, 3.922235, 1.991078, 2.624355, 2.623265, 2.620761, 2.623265, 1.654701, 2.623265, 2.623265, 1.989118, 1.653858]
mcf_values = [1.154747, 1.140655, 1.154434, 1.114332, 1.139768, 1.137877, 1.138424, 1.138344, 1.100838, 1.137877, 1.137876, 1.111727, 1.099413]

# Plotting the values
plt.figure(figsize=(10, 6))
plt.scatter(costs, bzip_values, color='b', label='bzip')
plt.scatter(costs, hmmer_values, color='g', label='hmmer')
plt.scatter(costs, libm_values, color='r', label='libm')
plt.scatter(costs, mcf_values, color='c', label='mcf')
plt.title('CPI vs. Costs for Different Benchmarks')
plt.xlabel('Cost')
plt.ylabel('Benchmark Value')
plt.grid(True)
plt.xticks(costs, rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('cpi_vs_costs_all.png')
plt.show()