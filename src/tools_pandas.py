import pandas as pd


def xlsx_to_csv(filename, extension):

    file_output = f'{filename}.csv'

    data = pd.read_excel(f'{filename}.{extension}')
    data.to_csv(
        file_output, encoding='utf-8', float_format='%.2f', header=True, index=False,
    )

    return file_output


def dictionary_to_csv(data, filename):
    data = pd.DataFrame(data)
    file_output = f'{filename}.csv'

    data.to_csv(
        file_output, encoding='utf-8', float_format='%.2f', header=True, index=False,
    )

    return file_output


def build_dataframe_from_csv(filename):
    return pd.read_csv(filename, engine='python').dropna(axis='columns')


def rename_columns_dataframe(data, columns):
    return data.rename(columns=columns)

def format_columns_dataframe(data, columns):
    return data.style.format(columns)
