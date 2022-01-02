class Dive():
    def read_input_dive_instructions_input(file_path):
        file = open(file_path, "r")
        diveInstruction = [(line.strip()).split() for line in file]
        file.close()
        return diveInstruction

    def get_horizontal_position(diveInstruction):
        horizontal_position = 0
        for instruction in diveInstruction:
            if instruction[0] == 'forward':
                horizontal_position += int(instruction[1])
        return horizontal_position

    def get_final_depth(diveInstruction):
        depth = 0
        for instruction in diveInstruction:
            if instruction[0] == 'down':
                depth += int(instruction[1])
            if instruction[0] == 'up':
                depth -= int(instruction[1])
        return depth

    def get_horizontal_and_depth_position_with_aim(diveInstruction):
        aim = 0
        horizontal_position = 0
        depth = 0
        for instruction in diveInstruction:
            if instruction[0] == 'forward':
                horizontal_position += int(instruction[1])
                depth += int(instruction[1]) * aim
            if instruction[0] == 'down':
                aim += int(instruction[1])
            if instruction[0] == 'up':
                aim -= int(instruction[1])
        return [horizontal_position, depth]

    if __name__ == '__main__':
        diveInstruction = read_input_dive_instructions_input(
                            'resources/day2/diveInstructions.txt')

        print('Result PartI: ', get_horizontal_position(diveInstruction) *
              get_final_depth(diveInstruction))
        result = get_horizontal_and_depth_position_with_aim(diveInstruction)
        print('Result PartII: ', result[0] * result[1])
