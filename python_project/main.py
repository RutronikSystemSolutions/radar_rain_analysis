# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

import matplotlib.pyplot as plt

import bgt60ltr11aip_reader
import bgt24_reader
import minew_me73ms01_reader
import bgt60tr13c_reader

doBgt60ltr11aip = False
doBgt24sense2golPulse = False
doMineW = False
doBgt60tr13c = True

# Set it to true if you want to have one plot per file
# If set to False, generate a plot with all the signals per sensor
generateSinglePlot = True

if (doBgt60ltr11aip == True):
    fileNames = ["bgt60ltr11aip/no_motion20250522-144102.raw.txt",
                "bgt60ltr11aip/motion_lateral_2m20250522-144142.raw.txt",
                "bgt60ltr11aip/motion_2m_1m_2m20250522-144243.raw.txt",
                "bgt60ltr11aip/nomotion_water20250522-144327.raw.txt",
                "bgt60ltr11aip/motion_2m_1m_2m_water20250522-144450.raw.txt"]

    labels = ["no motion",
            "motion lateral",
            "motion frontal",
            "no motion with water",
            "motion frontal with water"]
    
    if (generateSinglePlot == True):
        for i in range(len(fileNames)):
            plt.figure()
            plt.title("BGT60LTR11AIP " + labels[i])
            fileName = fileNames[i]
            amplitude = bgt60ltr11aip_reader.bgt60ltr11aip_reader_read_file(fileName)
            plt.plot(amplitude)
            plt.xlabel("Frame index")
            plt.ylabel("Magnitude")
            plt.ylim((0, 25))
            plt.grid(True)

    else:
        plt.figure()
        plt.title("BGT60LTR11AIP")
        for i in range(len(fileNames)):
            fileName = fileNames[i]
            amplitude = bgt60ltr11aip_reader.bgt60ltr11aip_reader_read_file(fileName)
            plt.plot(amplitude, label=labels[i])
            
        plt.legend()
        plt.xlabel("Frame index")
        plt.ylabel("Magnitude")
        plt.grid(True)

if (doBgt24sense2golPulse == True):
    fileNames = ["bgt24_sense2gol_pulse/nomotion.txt",
                "bgt24_sense2gol_pulse/motion_lateral_2m.txt",
                "bgt24_sense2gol_pulse/motion_2m_1m_2m.txt",
                "bgt24_sense2gol_pulse/nomotion_water.txt",
                "bgt24_sense2gol_pulse/motion_2m_1m_2m_water.txt"]

    labels = ["no motion",
            "motion lateral",
            "motion frontal",
            "no motion with water",
            "motion frontal with water"]

    if (generateSinglePlot == True):
        for i in range(len(fileNames)):
            plt.figure()
            plt.title("Sens2GOL Pulse " + labels[i])
            fileName = fileNames[i]
            amplitude = bgt24_reader.bgt24_reader_read_file(fileName)
            plt.plot(amplitude)
            plt.xlabel("Frame index")
            plt.ylabel("Magnitude")
            plt.ylim((0, 25))
            plt.grid(True)

    else:
        plt.figure()
        plt.title("Sens2GOL Pulse")
        for i in range(len(fileNames)):
            fileName = fileNames[i]
            amplitude = bgt24_reader.bgt24_reader_read_file(fileName)
            plt.plot(amplitude, label=labels[i])
            
        plt.legend()
        plt.xlabel("Frame index")
        plt.ylabel("Magnitude")
        plt.grid(True)

if (doMineW == True):
    fileNames = ["minew_me73ms01/nomotion.csv",
                "minew_me73ms01/motion_lateral_2m.csv",
                "minew_me73ms01/motion_2m_1m_2m.csv",
                "minew_me73ms01/nomotion_water.csv",
                "minew_me73ms01/motion_2m_1m_2m_water.csv"]

    labels = ["no motion",
            "motion lateral",
            "motion frontal",
            "no motion with water",
            "motion frontal with water"]
    
    if (generateSinglePlot == True):
        for i in range(len(fileNames)):
            plt.figure()
            plt.title("MineW ME73MS01 " + labels[i])
            fileName = fileNames[i]
            amplitudeMacro, amplitudeMicro, distanceMacro, distanceMicro = minew_me73ms01_reader.minew_me73ms01_reader_read_file(fileName)
            plt.plot(amplitudeMacro)
            plt.xlabel("Frame index")
            plt.ylabel("Magnitude")
            plt.ylim((0, 20000))
            plt.grid(True)

    else:
        plt.figure()
        plt.title("MineW ME73MS01")
        for i in range(len(fileNames)):
            fileName = fileNames[i]
            amplitudeMacro, amplitudeMicro, distanceMacro, distanceMicro = minew_me73ms01_reader.minew_me73ms01_reader_read_file(fileName)
            plt.plot(amplitudeMacro, label=labels[i])
            
        plt.legend()
        plt.xlabel("Frame index")
        plt.ylabel("Magnitude")
        plt.grid(True)

if (doBgt60tr13c == True):
    fileNames = ["bgt60tr13c/nomotion20250522-145157",
                "bgt60tr13c/motion_lateral_2m20250522-145229",
                "bgt60tr13c/motion_2m_1m_2m20250522-145320",
                "bgt60tr13c/nomotion_water20250522-145406",
                "bgt60tr13c/motion_2m_1m_2m_water20250522-145639"]

    labels = ["no motion",
            "motion lateral",
            "motion frontal",
            "no motion with water",
            "motion frontal with water"]

    if (generateSinglePlot == True):
        for i in range(len(fileNames)):
            plt.figure()
            plt.title("BGT60TR13C " + labels[i])
            fileName = fileNames[i]
            amplitude, speedOverTime, rangeOverTime = bgt60tr13c_reader.bgt60tr13c_amplitude_from_directory(fileName)
            plt.plot(amplitude)
            plt.xlabel("Frame index")
            plt.ylabel("Magnitude")
            plt.ylim((0, 35))
            plt.grid(True)

    else:
        plt.figure()
        plt.title("BGT60TR13C")
        for i in range(len(fileNames)):
            fileName = fileNames[i]
            amplitude, speedOverTime, rangeOverTime = bgt60tr13c_reader.bgt60tr13c_amplitude_from_directory(fileName)
            plt.plot(amplitude, label=labels[i])

        plt.legend()
        plt.xlabel("Frame index")
        plt.ylabel("Magnitude")
        plt.grid(True)

plt.show()