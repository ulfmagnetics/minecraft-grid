from argparse import ArgumentParser
from utils import MAP_SIZES
from map import Map

# This script lists the coordinates covered by each possible Minecraft map at the specified zoom level.

print('----------------------------')
print('~~ Minecraft grid utility ~~')
print('----------------------------')

parser = ArgumentParser(description='List the grid coordinates covered by various Minecraft maps.')
parser.add_argument('-z', '--zoom-level', type=int, dest='zoom_level', default=0, help='Zoom level to use (0-4)')
#parser.add_argument('-o', '--origin', dest='origin', default='0,0', help='Origin point to use for generating coordinates')
parser.add_argument('-s', '--steps', type=int, dest='num_steps', default=1, help='Number of map tiles to cover in each direction from origin')
args = parser.parse_args()

if args.zoom_level < 0 or args.zoom_level >= len(MAP_SIZES):
    parser.exit('Invalid zoom level. Select a level between 0 and %d.' % (len(MAP_SIZES)-1))

print('Using zoom level %d (size=%d)' % (args.zoom_level, MAP_SIZES[args.zoom_level]))
print('* dumping tiles...')

i = 1
for m in range(-args.num_steps, args.num_steps+1):
    for n in range(-args.num_steps, args.num_steps+1):
        print('Map tile #%d (m=%d,n=%d)' % (i, m, n))
        map_tile = Map(m, n, MAP_SIZES[args.zoom_level])
        bounds = map_tile.bounds()
        print('%5d,%5d -> %5d,%5d' % bounds)
        i = i + 1
