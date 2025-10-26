def calculate_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2)**0.5

def get_location(location_name):
    return f"Location: {location_name}"

