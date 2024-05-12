districts = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
populations = [247100, 333300, 266800, 420900, 318000]
max_population_index = populations.index(max(populations))
min_population_index = populations.index(min(populations))
print("Quận có dân số cao nhất là:", districts[max_population_index], "tại vị trí:", max_population_index)
print("Quận có dân số thấp nhất là:", districts[min_population_index], "tại vị trí:", min_population_index)
print("Quận có dân số cao nhất là:", districts[max_population_index])
print("Quận có dân số thấp nhất là:", districts[min_population_index])
