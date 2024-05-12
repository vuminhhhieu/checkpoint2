populations = [247100, 333300, 266800, 420900, 318000]
areas = [9.224, 43.35, 12.04, 9.96, 10.09]
population_densities = []
for i in range(len(populations)):
    density = populations[i] / areas[i]
    population_densities.append(density)
# print("Mật độ dân số của các quận là:", population_densities)
total_density = sum(population_densities)
average_density = total_density / len(population_densities)
print("Mật độ dân số trung bình của các quận là:", average_density)
