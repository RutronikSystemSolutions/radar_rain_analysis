# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

import numpy as np
import json
import radarprocessor
import stats
import arrayutils

# Load radar measurement values
def bgt60tr13c_load_from_directory(directory_path):
    file_path = directory_path + "\\RadarIfxAvian_00\\radar.npy"
    radar_data = np.load(file_path)
    return radar_data

# Load radar configuration
def bgt60tr13c_load_config_from_directory(directory_path):
    file_path = directory_path + "\\RadarIfxAvian_00\\config.json"
    f = open(file_path)
    config = json.load(f)
    f.close()
    return config

def bgt60tr13c_amplitude_from_directory(fileDir):
    radar_data = bgt60tr13c_load_from_directory(fileDir)
    radar_config = bgt60tr13c_load_config_from_directory(fileDir)

    processor = radarprocessor.RadarProcessor()
    processor.set_data_and_config(radar_data, radar_config)
    frameCount = len(radar_data)
    antennaIndex = 0
    rangeFFTLen = processor.get_range_fft_len()
    chirpsPerFrame = processor.get_chirps_per_frame()
    chirpRepetitionTime = processor.get_chirps_repetition_time()
    frameRepetitionTime = processor.get_frame_repetition_time()
    maxrange = processor.get_max_range()

    celerity = 299792458
    groundfreq = 60000000000
    lambdaval = celerity / groundfreq

    vmin = -lambdaval / (4 * chirpRepetitionTime)
    vmax = lambdaval / (4 * chirpRepetitionTime)
    vres = (vmax - vmin) / chirpsPerFrame

    maxAmplitudeOverTime = []
    speedOverTime = []
    rangeOverTime = []

    # For each frame compute Doppler FFT
    for frameIndex in range(frameCount):
        # First get the range FFT (for every chirp within the frame)
        # Size of the array [chirps per frame][fft len]
        # with fft len = (samples per chirp / 2) + +1
        frameRangeFFT = processor.get_frame_range_fft(frameIndex, antennaIndex)

        dopplerFFTValues = []

        # For each bin (or range/distance)
        for binIndex in range(rangeFFTLen):
            binContent = []

            # Extract the complex value over the chirps
            for chirpIndex in range(chirpsPerFrame):
                binContent.append(frameRangeFFT[chirpIndex][binIndex])

            # Compute average
            avgComplex = stats.avg(binContent)
            binFormatted = arrayutils.apply_offset(binContent, -avgComplex)

            # Compute doppler FFT (one per bin)
            fftout = np.fft.fftshift(np.fft.fft(binFormatted))
            dopplerFFTValues.append(fftout)

        # Get max amplitude
        # maxValue = arrayutils.get_matrix_max(np.abs(dopplerFFTValues))
        maxValue, maxSpeed, maxDistance = arrayutils.get_matrix_max_with_index(np.abs(dopplerFFTValues))
        maxAmplitudeOverTime.append(maxValue)
        speedOverTime.append(maxSpeed)
        rangeOverTime.append(maxDistance)

    return maxAmplitudeOverTime, speedOverTime, rangeOverTime