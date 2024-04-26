from Vehicle import Bike, Car, Scooty


def main():
    bike = Bike("Red", 2, 5)
    car = Car("Blue", 4, 6)
    scooty = Scooty("Green", 2, 4)

    bike.display_details()
    print("\n")
    car.display_details()
    print("\n")
    scooty.display_details()


if __name__ == "__main__":
    main()
