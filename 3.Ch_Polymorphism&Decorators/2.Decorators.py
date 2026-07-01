def my_decorator(fx):
    def main_function(*args): #los args de la funcion
        print("Before calling the function")
        response = fx(*args)
        print("After calling the function")
        return response
    return main_function

@my_decorator
def fetch_data(url:str,path:str):
    print("En la mitad")
    return f"fetching data from {url} and saving in {path}"

response = fetch_data("https://data.com","/tmp/data.json")
print(response)

def pandas_decorator(fx):
    def mainfunc(*args):
        response = fx(*args)
        response.to_parquet("3.Ch_Polymorphism&Decorators\\temp.parquet")
        return response 
    return mainfunc
@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df
responde = csv_to_parquet("3.Ch_Polymorphism&Decorators\\orders.csv")
print(responde.head)

