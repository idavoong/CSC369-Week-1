import sys
import csv
import time

if __name__ == "__main__":
    start = sys.argv[1] + " " + sys.argv[2]
    end = sys.argv[3] + " " + sys.argv[4]

    if start >= end:
        print("Start date must be before end date")
        exit()

    colors = {}
    locations = {}

    start_time = time.perf_counter_ns()

    with open('2022_place_canvas_history.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            color = row[2]
            location = row[3]

            if start <= row[0] <= end:
                if color not in colors.keys():
                    colors[color] = 1
                else:
                    colors[color] += 1

                if location not in locations.keys():
                    locations[location] = 1
                else:
                    locations[location] += 1

    # print(colors)
    # print(locations)

    greatest_color = max(colors, key=colors.get)
    greatest_location = max(locations, key=locations.get)

    end_time = time.perf_counter_ns()

    elapsed_time_ms = (end_time - start_time) / 1000000

    print("Most placed color: ", greatest_color)
    print("Most placed pixel location: ", greatest_location)
    print("Time taken: ", elapsed_time_ms, "ms")