#sudo apt install python-pip
#pip install coloredlogs
import os
import sys
import coloredlogs, logging
import colored_traceback
from termcolor import colored
from colorama import Fore, Back, Style

import backtrace

backtrace.hook(
    reverse=True,
    align=True,
    strip_path=True,
    enable_on_envvar_only=True,
    on_tty=True,
    conservative=True,
    styles={
        'backtrace': Fore.YELLOW + '{0}',
        'error': Fore.RED + Style.BRIGHT + '{0}',
        'line': Fore.RED + Style.BRIGHT + '{0}',
        'module': '{0}',
        'context': Style.BRIGHT + Fore.GREEN + '{0}',
        'call': Fore.YELLOW + '--> ' + Style.BRIGHT + '{0}'
    })


colored_traceback.add_hook(always=True)



# Create a logger object.
logger = logging.getLogger(__name__)

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
coloredlogs.install(level='DEBUG')

# If you don't want to see log messages from libraries, you can pass a
# specific logger object to the install() function. In this case only log
# messages originating from that logger will show up on the terminal.
coloredlogs.install(level='DEBUG', logger=logger)

# Some examples.
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")





print colored("""hello
              hellow""", 'red'), colored('world', 'green')

backtrace.unhook()