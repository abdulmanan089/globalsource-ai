def filter_suppliers(data):

    results = []

    for item in data:

        score = 80

        results.append({
            "product": item["product"],
            "price": item["price"],
            "moq": item["moq"],
            "rating": score
        })

    return results