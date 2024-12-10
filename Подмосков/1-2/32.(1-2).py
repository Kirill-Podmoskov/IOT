def filter_(filename, threshold):
    filtered_frequencies = []
    with open(filename, 'r') as file:
        for line in file:
            frequencies = line.strip().split(';')
            for freq_str in frequencies:
                freq = float(freq_str)
                if freq < threshold:
                    filtered_frequencies.append(freq)
    result = ' '.join(map(str, filtered_frequencies))
    return result

filename = "32.freqs.txt"

threshold = float(input("Укажите верхний порог частот "))
filtered_result = filter_(filename, threshold)
print(filtered_result)

