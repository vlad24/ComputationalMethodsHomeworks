def caluclate_differnces(coefficients):
    deltas = []
    for i in range(len(coefficients) - 1):
        deltas.append((coefficients[i + 1] - (coefficients[i])))
        #deltas.append((floor(coefficients[i + 1] * 10**6) - floor((coefficients[i])*10**6)) / 1000000)
    return deltas

if __name__ == '__main__':
    start_array = [1614419, 1656832, 1694888, 1728606, 1758030, 1783225, 1804279, 1821299, 1834414, 1843768]
    tmp_array = start_array
    for j in range(len(start_array)):
        offset = [" " for i in range(j)]
        print("".join(offset),tmp_array)
        tmp_array = caluclate_differnces(tmp_array)
    