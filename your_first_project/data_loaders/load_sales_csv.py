import pandas as pd
import re
from unidecode import unidecode
from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    filepath = 'your_first_project/Ventas Octubre-Junio Input2.csv'
    
    df_limpieza = pd.read_csv(filepath, encoding = 'cp1252')

    new_names = [transformCol(col) for col in df_limpieza.columns]
    df_limpieza.columns = new_names
    df_limpieza = df_limpieza.applymap(transform_data)

    return df_limpieza

def transformCol(col_name):
    col_name = col_name.upper()
    col_name = unidecode(col_name)
    col_name = col_name.replace(' ', '_')
    col_name = re.sub(r'\W+', '', col_name)
    return col_name

def transform_data(value):
    if isinstance(value, str):
        return value.capitalize()
    return value

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
