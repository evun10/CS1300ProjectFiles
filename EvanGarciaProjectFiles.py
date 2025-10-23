
def main():
    print("Project Files by Evan Garcia")
    displayTemparature()

# displayTemparature will display the temparature's from the AtlantaTemps2017.csv file.
def displayTemparature():
    file = open("AtlantaTemps2017.csv", "r")
    highestTemp = None
    lowestTemp = None
    lowestHighTemp = None
    HighestLowTemp = None

    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        date = parts[0]
        high = int(parts[1])
        low = int(parts[2])

        if highestTemp is None or high > highestTemp:
            highestTemp = high
            highestDate = date

        elif lowestTemp is None or low > lowestTemp:
            lowestTemp = low
            lowestDate = date

        elif lowestHighTemp is None or high < lowestHighTemp:
            lowestHighTemp = high
            lowestHighDate = date

        elif HighestLowTemp is None or low < HighestLowTemp:
            HighestLowTemp = low
            highestLowDate = date

    print("The highest temparature of the year", highestTemp, "on", highestDate)
    print("The lowest temparature of the year", lowestTemp, "on", lowestDate)
    print("The lowest high temparature of the year", lowestHighTemp, "on", lowestHighDate)
    print("The highest low temparature of the year", HighestLowTemp, "on", highestLowDate)

    file.close()
main()