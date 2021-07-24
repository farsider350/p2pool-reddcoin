from p2pool.bitcoin import networks

PARENT = networks.nets['reddcoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 2*24*60 # shares
REAL_CHAIN_LENGTH = 2*24*60 # shares
TARGET_LOOKBEHIND = 60 # shares
SPREAD = 8 # blocks
IDENTIFIER = 'e037d5b8c6923310'.decode('hex')
PREFIX = '7208c1a53ef639b0'.decode('hex')
P2P_PORT = 2017
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 2018
BOOTSTRAP_ADDRS = '139.180.181.92'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-reddcoin'
VERSION_CHECK = lambda v: None if 170401 <= v else 'Reddcoin version too old. Upgrade to 0.17.4.1 or newer!'
VERSION_WARNING = lambda v: None
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
