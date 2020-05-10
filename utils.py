# Define some utility functions and constants

# Map sizes at zoom levels 0-4
MAP_SIZES = [128, 256, 512, 1024, 2048]

# From https://minecraft.gamepedia.com/Tutorials/Mapping:
# The top left corner of each map now aligns to the (x,z) coordinate (-64, -64) +- (m,n)*size.
def top_left_coordinate(m, n, size):
    return (m * size - 64, n * size - 64)
