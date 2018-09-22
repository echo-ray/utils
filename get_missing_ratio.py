def get_missing_ratio(data):
    '''
    for pre-processing data
    
    input: pandas DataFrame
    return: pandas DataFrame, 
       index | col | missing ratio | unique data
    '''
    info = {}
    
    for col in data.columns:
        row = data.shape[0]
        unique = data.groupby(col).size()
        
        if len(unique) > 20:
            unique = unique[:5]
        unique = unique.to_dict()
        
        total_amount = sum(unique.values())
        missing_row = row - total_amount
        missing_ratio = round((missing_row / row)*100, 2)
        
        info[col] = {
            'col':col, 'missing_row':missing_row, 
            'missing_ratio':missing_ratio, 'unique':unique
        }
        #print(f"{col:15}|{missing_ratio:>5.2f}%|", unique)
        
    return pd.DataFrame(info).T.sort_values(by='missing_ratio', ascending=False)
