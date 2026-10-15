from data.data import data
from tools.func import display_result


def describe_field(field, describe: str, show_result: bool = True) -> dict:
    "Calculate a descriptive statistic for a selected field."

    dataset = data.get_data()

    # calculate
    result = dataset.describe()[field][describe]

    # show
    if show_result == True:
        display_result(field, describe, result)

    return {"field": field, "describe": describe, "result": result}


def quartiles(field, show_result: bool = True) -> dict:
    "Calculate a quartiles for a selected field."

    dataset = data.get_data()

    # calcualte
    qs = ["25%", "50%", "75%"]

    rs = []
    for q in qs:
        rs.append(dataset.describe()[field][q])

    # show
    if show_result:
        print("=== Analysis result ===")
        print(f"Field: {field}")
        print(f"Statistic: quartiles")

        for i in range(len(qs)):
            print(f"Result ({qs[i]}): {rs[i] * 1000000:,.0f} units")

    return {"field": field, "describe": "quartiles", "result": rs}
