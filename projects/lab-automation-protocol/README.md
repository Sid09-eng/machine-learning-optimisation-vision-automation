# Laboratory Automation Protocol

## Problem

I wrote a two-row colour-gradient protocol for a 96-well plate.

## Approach

Four source colours fill the first row with set volumes. The second row runs in reverse to create the mirror image. I use one tip per colour to reduce carryover, and every well receives 250 µL in total.

## Skills

- Python protocol development
- Opentrons API and deck-layout definition
- Volume accounting and plate-coordinate mapping
- Experimental automation documentation

## Source and data

I wrote the protocol against the Opentrons API using named standard labware. It does not include private results or hardware logs.

## Reproduce

Check the deck, labware, pipette, reservoir, and starting-tip settings in the protocol. Run the Opentrons simulator and complete local safety checks before using a robot.

## Limits

The code describes transfers; it does not prove that a robot run succeeded. Labware calibration, reagent compatibility, robot setup, tips, and lab approval still matter.
