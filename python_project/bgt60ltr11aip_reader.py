# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

import complex_numbers
import numpy as np
import arrayutils
import stats
from scipy import signal

def bgt60ltr11aip_reader_get_frames(path):
    frames = []

    with open(path, newline='') as file:
        content = file.readlines()

        waitingFirstFrame = True

        frameI = []
        frameQ = []

        waitingI = True

        # No need to start at index 0, first frame starts at index 20 (line 21)
        for lineIndex in range(20, len(content)):
            if ("Frame_Number =" in content[lineIndex]):
                # New frame starts here
                if (waitingFirstFrame == True):
                    waitingFirstFrame = False
                else:
                    frames.append([frameI, frameQ])
                    # create new frame
                    frameI = []
                    frameQ = []
                    waitingI = True

            elif ("#" in content[lineIndex]):
                # Do nothing, it is part of header
                pass

            else:
                if (waitingI == True):
                    waitingI = False
                    frameI.append(float(content[lineIndex]))
                else:
                    waitingI = True
                    frameQ.append(float(content[lineIndex]))

            
        # Last one
        frames.append([frameI, frameQ])

    return frames

def bgt60ltr11aip_reader_read_file(path):
    frames = bgt60ltr11aip_reader_get_frames(path)
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
