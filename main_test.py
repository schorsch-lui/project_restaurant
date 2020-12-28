import pandas as pd

csv_path = "data//fast_food_restaurants.csv"

df = pd.read_csv(csv_path)

print(df.head())

df.drop("name", axis=1, inplace=True)


def select_relevant_columns(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    rel_cols = [
        "name",
        "address",
        "postalCode",
        "city",
        "latitude",
        "longitude",
        "categories",
    ]

    try:
        df = df[rel_cols].copy()
    except KeyError:

        msg = f"""Data needs to have at least the following columns: {', '.join(rel_cols)}
               """
        raise KeyError(msg)
    return df


df_new = select_relevant_columns(df)
print(df_new.head())
