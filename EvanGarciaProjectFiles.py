
def main():
    print("Project Files by Evan Garcia")
    displayTemparature()

# PART 1: displayTemparature will display the temparature's from the AtlantaTemps2017.csv file.
def displayTemparature():
    file = open("AtlantaTemps2017.csv", "r")

    highestTemp = None
    highestTempDate = ""
    lowestTemp = None
    lowestTempDate = ""
    lowestHighTemp = None
    lowestHighTempDate = ""
    HighestLowTemp = None
    highestLowTempDate = ""

    highestSum = 0
    lowestSum = 0
    count = 0

    highTemps = []
    lowTemps = []

    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        date = parts[0]
        high = int(parts[1])
        low = int(parts[2])

        highestSum += high
        lowestSum += low
        count += 1

        highTemps.append(high)
        lowTemps.append(low)

        if highestTemp is None or high > highestTemp:
            highestTemp = high
            highestTempDate = date

        if lowestTemp is None or low < lowestTemp:
            lowestTemp = low
            lowestTempDate = date

        if lowestHighTemp is None or high < lowestHighTemp:
            lowestHighTemp = high
            lowestHighTempDate = date

        if HighestLowTemp is None or low > HighestLowTemp:
            HighestLowTemp = low
            highestLowTempDate = date

    file.close()

    averageHighTemps = highestSum / count
    averageLowTemps = lowestSum / count

    print("The highest temparature of the year", highestTemp, "and occured on", highestTempDate)
    print("The lowest temparature of the year", lowestTemp, "and occured on", lowestTempDate)
    print("The lowest high temparature of the year", lowestHighTemp, "and occured on", lowestHighTempDate)
    print("The highest low temparature of the year", HighestLowTemp, "and occured on", highestLowTempDate)
    print("The average high temparature for the year:", round(averageHighTemps, 2))
    print("The average low temparature for the year:", round(averageLowTemps, 2))

    lowThreshold = int(input("Enter a low temparature threshold: "))
    highThreshold = int(input("Enter a high temparature threshold: "))

    lowCount = 0
    for temparature in lowTemps:
        if temparature < lowThreshold:
            lowCount = lowCount + 1

    highCount = 0
    for temparature in highTemps:
        if temparature > highThreshold:
            highCount = highCount + 1

    print("Number of low temparature's below", lowThreshold, ":", lowCount)
    print("Number of high temparature's above", highThreshold, ":", highCount)
main()