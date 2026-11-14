# Laboratory Automation Protocol

## Problem

Define a repeatable two-row colour-gradient liquid-handling protocol for a 96-well plate.

## Approach

Four source colours are dispensed across one row using explicit per-well volumes; a second row is filled in reverse order to create a mirrored gradient. One tip is used per source colour to reduce source carryover, and every target well totals 250 µL.

## Skills

- Python protocol development
- Opentrons API and deck-layout definition
- Volume accounting and plate-coordinate mapping
- Experimental automation documentation

## Source and data

The protocol logic is authored for the Opentrons API using named standard labware definitions. No proprietary experimental results or hardware logs are included.

## Reproduce

Review deck, labware, pipette, reservoir, and starting-tip assumptions in the project protocol. Validate in the Opentrons simulator and perform local laboratory safety review before any physical run.

## Limits

This code defines a transfer plan; it does not prove a successful physical run. Labware calibration, reagent compatibility, robot configuration, tip availability, and laboratory approval remain required.
