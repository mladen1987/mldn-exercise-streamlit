def ensure_list(x):
    if x is None:
        return None
    return x if isinstance(x, list) else [x]
