from geo import hello
from geo.utils import calculate_distance, get_location

def main():
    print("=== Geo Package Test ===")
    print(hello())
    print(calculate_distance(0, 0, 3, 4))
    print(get_location("Seoul"))

if __name__ == "__main__":
    main()

