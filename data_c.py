import pandas as pd 

def get_data():
    
    df = pd.read_csv('fire.csv')

    year            = df['year'].tolist()

    wildfires    = df['wildfires'].tolist()

    result_dict = {
            'year'            :  year,
        'wildfires'    : wildfires
        
    }

    #print(result_dict)

    return result_dict

def add_row (year, wildfires):

    df = pd.read_csv('fire.csv') 

    new_row = {
    
            'year'       :   year, 
        'wildfires'    : wildfires
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('fire.csv')

if __name__ == "__main__":
    get_data()
    