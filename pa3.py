def get_checkin_bags(bag_weights, min_weight, max_weight):
    bags = []
    for idx in range(len(bag_weights)):
        weight = bag_weights[idx]

        if weight >= min_weight and weight <= max_weight:
            bags += [weight]

    return bags

bag_weights = [30.6, 21.1, 35.0]
min_weight = 35.0
max_weight = 35.0
print(get_checkin_bags(bag_weights, min_weight, max_weight))
