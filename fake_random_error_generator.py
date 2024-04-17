#https://peps.python.org/pep-0008/
import numpy as np
import pandas as pd


#CONST
XYZ_SIZE = 2**10
MEAN = 0
STD_DEV = 0.7

def generate_xy_vectors():
    x = np.arange(-XYZ_SIZE/2, XYZ_SIZE/2, 1)
    y= np.arange(-XYZ_SIZE/2, XYZ_SIZE/2, 1)
    return x, y

def generate_random_error():
    z = np.random.normal(MEAN, STD_DEV, XYZ_SIZE)
    return z

def write_to_csv():
    csv_columns = {'X' , 'Y', 'ERROR'}
    x_vector, y_vector = generate_xy_vectors()
    error_vector = generate_random_error()

    df = pd.DataFrame(columns=csv_columns)

    for column, value in zip(csv_columns, np.vstack((x_vector, y_vector, error_vector))):
        df[column] = value

    print(df)
    df.to_csv('Errors.csv', index=False)

write_to_csv()
