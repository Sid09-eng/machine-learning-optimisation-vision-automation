"""Opentrons OT-2 protocol for a mirrored 96-well colour gradient."""

from opentrons import protocol_api


metadata = {
    "protocolName": "Mirrored Rainbow Colour Gradient",
    "author": "Siddharth Choudhary",
    "description": "Two 96-well-plate rows with one fresh tip per source colour.",
    "apiLevel": "2.13",
}


TOTAL_VOLUME_UL = 250
SOURCE_WELLS = ("A3", "B3", "A4", "B4")
GRADIENT_UL = (
    (250, 0, 0, 0),
    (180, 70, 0, 0),
    (115, 135, 0, 0),
    (45, 205, 0, 0),
    (0, 230, 20, 0),
    (0, 160, 90, 0),
    (0, 90, 160, 0),
    (0, 20, 230, 0),
    (0, 0, 205, 45),
    (0, 0, 135, 115),
    (0, 0, 70, 180),
    (0, 0, 0, 250),
)


def run(protocol: protocol_api.ProtocolContext):
    """Execute the specified deck layout and volume plan."""
    plate = protocol.load_labware("corning_96_wellplate_360ul_flat", "1")
    tiprack = protocol.load_labware("opentrons_96_tiprack_300ul", "11")
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "3")
    pipette = protocol.load_instrument("p300_single_gen2", "left", tip_racks=[tiprack])
    pipette.starting_tip = tiprack["A1"]

    left_to_right = plate.rows_by_name()["B"]
    right_to_left = plate.rows_by_name()["C"][::-1]
    for colour_index, source_well in enumerate(SOURCE_WELLS):
        pipette.pick_up_tip()
        for first_well, second_well, volumes in zip(left_to_right, right_to_left, GRADIENT_UL):
            volume = volumes[colour_index]
            if volume == 0:
                continue
            pipette.aspirate(volume, reservoir[source_well])
            pipette.dispense(volume, first_well)
            pipette.aspirate(volume, reservoir[source_well])
            pipette.dispense(volume, second_well)
        pipette.drop_tip()
