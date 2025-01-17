import matplotlib.pyplot as plt

# Data from the table
benchmarks = ['specbzip', 'spechmmer', 'speclibm', 'specmcf', 'specsjeng']
seconds_simulated = [0.083982, 0.059396, 0.174671, 0.064955, 0.513528]
cpi = [1.679650, 1.187917, 3.493415, 1.299095, 10.270554]
l1_dcache_miss_rate = [0.014798, 0.001637, 0.060972, 0.002108, 0.121831]
l1_icache_miss_rate = [0.000077, 0.000221, 0.000094, 0.023612, 0.000020]
l2_miss_rate = [0.282163, 0.077760, 0.999944, 0.055046, 0.999972]

# Function to create a histogram
def create_histogram(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.bar(benchmarks, data, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()

# Create histograms for each category
create_histogram(seconds_simulated, 'Seconds Simulated', 'Benchmark', 'Seconds', 'seconds_simulated_def.png')
create_histogram(cpi, 'CPI', 'Benchmark', 'CPI', 'cpi_def.png')
create_histogram(l1_dcache_miss_rate, 'L1 D-Cache Miss Rate', 'Benchmark', 'Miss Rate', 'l1_dcache_miss_rate_def.png')
create_histogram(l1_icache_miss_rate, 'L1 I-Cache Miss Rate', 'Benchmark', 'Miss Rate', 'l1_icache_miss_rate_def.png')
create_histogram(l2_miss_rate, 'L2 Miss Rate', 'Benchmark', 'Miss Rate', 'l2_miss_rate_def.png')

print("Histograms created successfully.")

