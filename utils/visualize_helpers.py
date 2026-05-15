def render_spark_bar(values, max_width=10):
    """
    Returns a list of strings representing a simple spark bar chart.
    """
    if not values:
        return []

    max_val = max(values)
    min_val = min(values)

    # Avoid division by zero
    if max_val == min_val:
        return ["█" * 3 for _ in values]

    bars = []
    for v in values:
        # normalize 0–1
        ratio = (v - min_val) / (max_val - min_val)

        # scale to width
        filled = int(ratio * max_width)
        filled = max(1, filled)  # always show something

        bars.append("█" * filled)

    return bars
