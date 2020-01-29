from pandas import *

def main():
    track_width = 0
    track_length = 0
    segment_length = 0
    segment_width = 0

    width = input("Enter width of track: ")
    track_width = int(width)

    length = input("Enter length of track: ")
    track_length = int(length)

    widthC = input("Enter how many segments are wide: ")
    segment_width = int(widthC)

    lengthC = input("Enter how many segments are long: ")
    segment_length = int(lengthC)

    Matrix = [[0 for x in range(0, segment_width)] for y in range(0, segment_length)]

    print(DataFrame(Matrix))


if __name__ == "__main__":
    main()
