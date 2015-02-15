import logging
import osmcmvs

logging.basicConfig(level=logging.INFO, format="%(message)s")
def run(a):
    # initialize OsmCMVS manager class
    manager = osmcmvs.OsmCmvs(a)

    # initialize PMVS input from Bundler output
    manager.doBundle2PMVS()

    # call PMVS
    manager.doCMVS()
