class SonarSweep():
    def read_depth_input(file_path):
        input_file = open(file_path, 'r')
        return input_file.readlines()

    def get_increases_amount(report):
        increases = 0
        for index, depth in enumerate(report):
            if index > 0 and int(depth) > int(report[index-1]):
                increases += 1
        return increases

    def get_sliding_window_increases_amount(report):
        increases = 0
        lastValue = 0
        for index, depth in enumerate(report):
            if int(index) < len(report) - 3:
                sliding_window_sum = int(depth) + \
                    int(report[index+1]) + int(report[index+2])
                if (sliding_window_sum > lastValue):
                    increases += 1
                lastValue = sliding_window_sum
        return increases

    if __name__ == '__main__':
        depth_measurement = read_depth_input('resources/day1/deepthInput.txt')
        print("Depth Measurement Increases: ",
              get_increases_amount(depth_measurement))
        print("Sum of Measurement in sliding window increases: ",
              get_sliding_window_increases_amount(depth_measurement))
