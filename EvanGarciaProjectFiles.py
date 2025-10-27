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

    theData = []

    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        date = parts[0]
        high = int(parts[1])
        low = int(parts[2])
        theData.append((date, high, low))

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
    
    displayMonthStats(theData)

    # Part 2 displayMonthStats function will display the high temp, low temp, average high temp, and average low temp in each month.
def displayMonthStats(theData):
    monthlyData = {}

    for date, high, low in theData:
        month = int(date.split("/")[0])
        if month not in monthlyData:
            monthlyData[month] = []
        monthlyData[month].append((date, high, low))

    theMonths = [
        "Janurary", "Feburary", "March",
        "April", "May", "June", "July", "August", 
        "September", "October", "November", 
        "December"
    ]

    for month in range(1, 13):
        if month not in monthlyData:
            continue

        monthlyRecords = monthlyData[month]
        monthlyHighs = []
        monthlyLows = []

        for record in monthlyRecords:
            date = record[0]
            high = record[1]
            low = record[2]

            monthlyHighs.append(high)
            monthlyLows.append(low)
        
        highestRecord = monthlyRecords[0]
        lowestRecord = monthlyRecords[0]

        for record in monthlyRecords:
            if record[1] > highestRecord[1]:
                highestRecord = record
            if record[2] < lowestRecord[2]:
                lowestRecord = record

        averageHighTemps = sum(monthlyHighs) / len(monthlyHighs)
        averageLowTemps = sum(monthlyLows) / len(monthlyLows)

        print(month)
        print("The highest temparature:", highestRecord[1], "occurred on", highestRecord[0])
        print("The lowest temparature:", lowestRecord[2], "occurred on", lowestRecord[0])
        print("Average high temparature:", round(averageHighTemps, 2))
        print("Average low temparature:", round(averageLowTemps, 2))
main()