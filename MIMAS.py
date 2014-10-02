#! /usr/bin/env python

"""
MIMAS - The Multi-resolution Image Mask for Aegean Software

Created: Paul Hancock, Oct 2014
"""

import argparse
import logging
import numpy as np
import sys
from AegeanTools.regions import Region

version='0.1'

#seems like this fails sometimes
try:
    import cPickle as pickle
except ImportError:
    import pickle

def mim2reg(mimfile,regfile):
    region=pickle.load(open(mimfile,'r'))
    region.write_reg(regfile)
    logging.info("Converted {0} -> {1}".format(mimfile,regfile))
    return


if __name__=="__main__":
    epilog='Regions are added/subtracted in the following order, +r -r +c -c +p -p. This means that you might have to take multiple passes to construct overly complicated regions.'
    parser = argparse.ArgumentParser(epilog=epilog,prefix_chars='+-')
    #tools for creating .mim files
    parser.add_argument('-o', dest='outfile', action='store', help='output filename [default=region.mim]', default='region.mim')
    parser.add_argument('-depth', dest='maxdepth',action='store', metavar='N', default=8, help='maximum nside=2**N to be used to represent this region. [Default=8]')
    parser.add_argument('+r', dest='add_region', action='append',
                        default=[], type=str, metavar='filename',nargs='*',
                        help='add a region specified by the given file (.mim format)')
    parser.add_argument('-r', dest='rem_region', action='append',
                        default=[], type=str, metavar='filename',nargs='*',
                        help='exclude a region specified by the given file ( .mim format)')
    #add/remove circles
    parser.add_argument('+c', dest='include_circles', action='append',
                        default=[], type=float, metavar=('ra','dec','radius'), nargs=3,
                        help='add a circle to this region (decimal degrees)')
    parser.add_argument('-c', dest='exclude_circles', action='append',
                        default=[],type=float, metavar=('ra','dec','radius'), nargs=3,
                        help='exclude the given circles from a region')

    #add/remove polygons
    # parser.add_argument('+p', dest='included_polygons', action='append',
    #                     default=[], type=float, metavar=('ra','dec'), nargs='*',
    #                     help='add a polygon to this region ( decimal degrees)')
    # parser.add_argument('-p', dest='excluded_polygons', action='append',
    #                     default=[], type=float, metavar=('ra','dec'), nargs='*',
    #                     help='remove a polygon from this region ( decimal degrees)')

    #tools that use .mim files
    parser.add_argument('--mim2reg',dest='mim2reg', action='append', type=str, metavar=('region.mim','region.reg'), nargs=2, help='convert region.mim into region.reg', default=[])

    #extras
    parser.add_argument('--debug', dest='debug', action='store_true', help='debug mode [default=False]', default=False)
    parser.add_argument('--version', action='version', version='%(prog)s '+version)
    results = parser.parse_args()

    logging_level = logging.DEBUG if results.debug else logging.INFO
    logging.basicConfig(level=logging_level, format="%(process)d:%(levelname)s %(message)s")
    logging.info("This is MIMAS {0}".format(version))

    if len(results.mim2reg)>0:
        for i,o in results.mim2reg:
            mim2reg(i,o)
        sys.exit()

    #create empty region
    region=Region(results.maxdepth)

    #add/rem all the regions from files
    for r in results.add_region:
        logging.info("adding region from {0}".format(r))
        r2=pickle.load(r)
        region.union(r2)

    for r in results.rem_region:
        logging.info("removing region from {0}".format(r))
        r2=pickle.load(r)
        region.without(r2)


    #add circles
    if len(results.include_circles)>0:
        ras,decs,radii=zip(*results.include_circles)
        ras=map(np.radians,ras)
        decs=map(np.radians,decs)
        radii=map(np.radians,radii)
        region.add_circles(ras,decs,radii)

    #remove circles
    if len(results.exclude_circles)>0:
        r2=Region(results.maxdepth)
        ras,decs,radii=zip(*results.exclude_circles)
        r2.add_circles(ras,decs,radii)
        region.without(r2)

    #write output
    pickle.dump(region,open(results.outfile,'w'))
    logging.info("Wrote {0}".format(results.outfile))
