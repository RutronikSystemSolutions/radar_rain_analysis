# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

# Read file and process it
# Returns: amplitude macro, amplitude micro, distance macro, distance micro
def minew_me73ms01_reader_read_file(path):
    amplitudeMacro = []
    amplitudeMicro = []
    distanceMacro = []
    distanceMicro = []

    with open(path, newline='') as file:
        content = file.readlines()

        # Skip the first line (header)
        for lineIndex in range(1, len(content)):
            splitted = content[lineIndex].split(';')
            amplitudeMacro.append(int(splitted[3]))
            amplitudeMicro.append(int(splitted[4]))
            distanceMacro.append(int(splitted[1]))
            distanceMicro.append(int(splitted[2]))

    return amplitudeMacro, amplitudeMicro, distanceMacro, distanceMicro