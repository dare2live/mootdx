from mootdx import config
from mootdx.consts import EX_HOSTS
from mootdx.consts import GP_HOSTS
from mootdx.consts import HQ_HOSTS
from mootdx.server import server
from mootdx.utils import get_config_path

# 延迟导入 capabilities，避免循环依赖但允许 from mootdx import capabilities
def __getattr__(name):
    if name == 'capabilities':
        from mootdx import capabilities
        return capabilities
    raise AttributeError(f"module 'mootdx' has no attribute {name}")

__version__ = '0.12.0'
__author__ = 'bopo.wang <ibopo@126.com>'
