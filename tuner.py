import tunerconfig as cfg

if cfg.pathToEarthNavData == "pathNotSet":
    print("ERROR: please set the path to your earth_nav.dat file")
    exit()

newNavText = ""
navFile = open(cfg.pathToEarthNavData, "r")


def my_replacer(my_newline, my_replacevalue, my_region, my_airport):
    for r in cfg.regionModifier:
        if r["region"] == my_region:
            my_newline[5] = r[my_replacevalue]

    for a in cfg.airportModifier:
        if a["icao"] == my_airport:
            my_newline[5] = a[my_replacevalue]

    return my_newline

# Loop over nav file
lineCount = 0;
for line in navFile:
    splittedLine = line.split()

    newLine = splittedLine

    if splittedLine and len(splittedLine) > 8:

        region = splittedLine[9]
        airport = splittedLine[8]

        if splittedLine[0] == "4":
            newLine = my_replacer(newLine, "loc", region, airport)
        if splittedLine[0] == "6":
            newLine = my_replacer(newLine, "gs", region, airport)
        if splittedLine[0] == "12":
            newLine = my_replacer(newLine, "ident", region, airport)


    newNavText += ' '.join(map(str, newLine))
    newNavText += '\n'

newNavFile = open(cfg.pathToEarthNavData, "w")
newNavFile.write(newNavText)