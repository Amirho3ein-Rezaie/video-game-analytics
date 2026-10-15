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

    rs = {}
    for q in qs:
        rs[q] = dataset.describe()[field][q]

    # show
    if show_result:
        print("=== Analysis result ===")
        print(f"Field: {field}")
        print(f"Statistic: quartiles")

        srs = list(rs.values())
        for i in range(len(qs)):
            print(f"Result ({qs[i]}): {srs[i] * 1000000:,.0f} units")

    return {"field": field, "describe": "quartiles", "result": rs}


def all(field, show_result: bool = True) -> dict:
    "calculate the all of descriptive stats."

    dataset = data.get_data()

    # calculate the stat
    result = {}
    stats = list(dataset.describe()[field].keys())
    for s in stats:
        result[s] = dataset.describe()[field][s]

    # show the stat
    if show_result:
        print("=== Analysis result ===")
        print(f"(field) : {field}")

        for key, value in result.items():
            if key != "count":
                print(f"({key}) : {value * 1000000:,.0f}")
            else:
                print(f"({key}) : {value:,.0f}")

    return result
