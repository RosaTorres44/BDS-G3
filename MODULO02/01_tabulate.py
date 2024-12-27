from tabulate import tabulate

data = [
    ["Alice", 24],
    ["Bob", 19],
    ["Charlie", 30]
]    

print(tabulate(data, headers=["Nombre", "Edad"], tablefmt="pretty"))