import logging
import osmbundler
import sys

logging.basicConfig(level=logging.INFO, format="%(message)s")

# initialize OsmBundler manager class
def run(a):
    print "inside runBundler"

    manager = osmbundler.OsmBundler(a)

    manager.preparePhotos()

    manager.matchFeatures()

    manager.doBundleAdjustment()
