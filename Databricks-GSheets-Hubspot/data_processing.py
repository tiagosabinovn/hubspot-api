import re

def cast_types(df, column_types_dict={}, return_all_columns=True):
    for col, col_type in column_types_dict.items():
        df = df.withColumn(col, F.col(col).cast(col_type))
    return df if return_all_columns else df.select(*column_types_dict.keys())

# Load Data from Google Sheets into Databricks

CARTERIZACAO_OFICIAL = "table.notes"
CARTERIZACAO_GSHEETS = "https://docs.google.com/spreadsheets/d/gsheets-id"
CARTERIZACAO_WORKSHEET = "Alfa"

CARTERIZACAO_GSHEETS_COLUMN_TYPES = {'primary': 'bigint', 'secundary': 'string'}

raw_carterizacao_df = gsheets_url_to_dataframe(CARTERIZACAO_GSHEETS, CARTERIZACAO_WORKSHEET)
raw_carterizacao_df = cast_types(raw_carterizacao_df, CARTERIZACAO_GSHEETS_COLUMN_TYPES, False)

new_columns = [re.sub(r'\\W+', '', col) for col in raw_carterizacao_df.columns]
carterizacao_df = raw_carterizacao_df.toDF(*new_columns)

carterizacao_df.write.mode("overwrite").option("mergeSchema", "true").saveAsTable("table.notes")

%sql
select * from table.notes

