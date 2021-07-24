import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 45444
ADDRESS_VERSION = 61
RPC_PORT = 2002
RPC_CHECK =RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'reddcoin' in (yield bitcoind.rpc_help()) 
            (yield helper.check_block_header(bitcoind, 'b868e0d95a3c3c0e0dadc67ee587aaf9dc8acbf99e3b4b3110fad4eb74c1decc')) and
                          (yield bitcoind.rpc_getinfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 10000*100000000 >> (height + 1)//210000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'RDD'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Reddcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Reddcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.reddcoin'), 'reddcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://'
ADDRESS_EXPLORER_URL_PREFIX = 'https://'
TX_EXPLORER_URL_PREFIX = 'https://'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
