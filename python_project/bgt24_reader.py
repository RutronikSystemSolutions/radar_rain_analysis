# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

import complex_numbers
import stats
import arrayutils
from scipy import signal
import numpy as np

# Read the frames from the given file
# Remark: a frame is composed of 4 signals:
# high gain I/Q
# low gain I/Q
def bgt24_reader_get_frames(path):
    frames = []

    with open(path, newline='') as file:
        content = file.readlines()
        # Extract frames
        waitingFirstFrame = True
        
        highGainI = []
        highGainQ = []
        lowGainI = []
        lowGainQ = []
        
        HIGHGAINI = 0
        HIGHGAINQ = 1
        LOWGAINI = 2
        LOWGAINQ = 3

        currentStatus = HIGHGAINI

        for lineIndex in range(len(content)):
            if ("Frame_Number =" in content[lineIndex]):
                if (waitingFirstFrame == True):
                    # First frame follows
                    waitingFirstFrame = False
                else:
                    frames.append([highGainI, highGainQ, lowGainI, lowGainQ])
                    
                    # Create new frame
                    highGainI = []
                    highGainQ = []
                    lowGainI = []
                    lowGainQ = []

                    currentStatus = HIGHGAINI
            else:
                if (waitingFirstFrame == False):
                    if (currentStatus == HIGHGAINI):
                        highGainI.append(float(content[lineIndex]))
                        if (len(highGainI) == 128):
                            currentStatus = HIGHGAINQ

                    elif (currentStatus == HIGHGAINQ):
                        highGainQ.append(float(content[lineIndex]))
                        if (len(highGainQ) == 128):
                            currentStatus = LOWGAINI

                    elif (currentStatus == LOWGAINI):
                        lowGainI.append(float(content[lineIndex]))
                        if (len(lowGainI) == 128):
                            currentStatus = LOWGAINQ

                    elif (currentStatus == LOWGAINQ):
                        lowGainQ.append(float(content[lineIndex]))

        # Last one
        frames.append([highGainI, highGainQ, lowGainI, lowGainQ])

    return frames

def bgt24_reader_read_file(path):
    frames = bgt24_reader_get_frames(path)
    amplitudes = []

    for frameIndex in range(len(frames)):
        complexNb = complex_numbers.complex_from_i_q_array(frames[frameIndex][0], frames[frameIndex][1])

        avg = stats.avg(complexNb)
        shiftedComplexNb = arrayutils.apply_offset(complexNb, -avg)
        window = signal.windows.blackmanharris(len(shiftedComplexNb))
        windowedSignal = arrayutils.mult_array(shiftedComplexNb, window)
        dft = np.fft.fft(windowedSignal)
        dft = np.abs(np.fft.fftshift(dft))
        # dft = 20 * np.log10(dft)

        maxValue = dft[0]
        for binIndex in range(len(dft)):
            if (dft[binIndex] > maxValue):
                maxValue = dft[binIndex]

        amplitudes.append(maxValue)

    return amplitudes