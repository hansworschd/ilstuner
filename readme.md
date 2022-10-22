# ILSTuner
This small python script can be used for an automatic extension of the default 18/30 miles of ILS systems in X-Plane.

## Description
The default range to receive an ILS signal in X-Plane 11 is 18 miles for GS and LOC and 30 miles for the identifier.
This is not too realistic, as even if the aviation authority defines the ILS range to be 18 miles, it can be received much further away.
Furthermore, virtual controllers might give you vectors beyond this range and it is not always easy to fly the final track accordingly.
Thats why I created such as a script to extend the ranges.
**Localizer only approaches are untouched at the moment!**

## Requirements
Tested with Python 3.9.2.
May work with other Python versions as well.

## Installation
1. Just copy the two files into any folder
2. Update the path to your earth_nav.dat in `tunerconfig.py` (Usually `C:\X-Plane 11\Custom Data\earth_nav.dat` or similar)

## Run
`python tuner.py`

## Config
You can define your own rules how the tuner script behaves.
Update the `tunerconfig.py` accordingly.
**Airport config will overwrite Region config.**