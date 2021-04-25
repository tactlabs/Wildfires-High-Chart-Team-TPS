import pandas as pd 

def get_data():
    
    df = pd.read_csv('CanadianMillionaires.csv')

    millionaire     = df['millionaire'].tolist()

    worth    = df['worth'].tolist()

    result_dict = {
            'millionaire'            : millionaire,
        'worth'    : worth
        
        }

    #print(result_dict)

    return result_dict

def add_row (millionaire, worth):

    df = pd.read_csv('CanadianMillionaires.csv') 

    new_row = {
    
            'millionaire':  millionaire, 
            'worth'    : worth
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('fire.csv')

if __name__ == "__main__":
    get_data()