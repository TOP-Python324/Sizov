def central_tendency(number1: float, number2: float, *numbers: float) -> dict[str, float]:
    """Вычисляет основные меры центральной тенденции для некоторого количества чисел"""
    
    out_dict = {'median': 0, 'arithmetic': 0, 'geometric': 0, 'harmonic': 0}
    in_tuple = (number1, number2) + numbers
    
    sum_geometric = 1 
    sum_harmonic = 0 
    
    for n in in_tuple:         
        sum_geometric *= n
        sum_harmonic += 1/n
        
    out_dict['arithmetic']  = sum(in_tuple) / len(in_tuple)  
    out_dict['geometric']  = pow(sum_geometric, 1/len(in_tuple))
    out_dict['harmonic']  = len(in_tuple) / sum_harmonic 
    
    in_tuple = sorted(in_tuple)
    if len(in_tuple)%2 != 0:
        out_dict['median'] = float(in_tuple[int((len(in_tuple) - 1)/2)])
    else:
        out_dict['median'] = (in_tuple[int(len(in_tuple)/2)] + in_tuple[int(len(in_tuple)/2 - 1)]) / 2    
        
    return out_dict
    
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
        
