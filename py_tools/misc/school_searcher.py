import pandas as pd

def search_csv_column(file_path: str, column_name: str, search_string: str) -> list:
    """Search a CSV file for a specific column and return the top 3 results."""
    
    dtype = {column_name: str, 'ADDRESS': str}
    usecols = [column_name, 'ADDRESS']
    
    df = pd.read_csv(file_path, engine="pyarrow", dtype=dtype, usecols=usecols)
    
    search_results = df[df[column_name].str.contains(search_string, case=False, na=False)]
    
    top_results = search_results[[column_name, 'ADDRESS']].head(3)

    if top_results.empty:
        return search_csv_column("static/schools/Private_Schools.csv", column_name, search_string)

    result_list = top_results.values.tolist()
    
    return result_list

def main() -> None:
    file_path = 'static/schools/Public_Schools.csv'
    column_name = 'NAME'
    search_string = 'John Adams'

    results = search_csv_column(file_path, column_name, search_string)
    
    if results:
        print(results)
    else:
        print("No matching results found.")

if __name__ == '__main__':
    main()
