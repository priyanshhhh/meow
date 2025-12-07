import sys
import asyncio
import traceback
from Meow.Core.logging import logger

# Dont let any single baddie get away
def fucking(loop, context):
    """Catch and fuck Baddie immediately"""
    exception = context.get('exception')
    if exception:
        logger.error(f"🥵 Big ass Baddie found: {exception}")
        logger.error(''.join(traceback.format_exception(type(exception), exception, exception.__traceback__)))
    else:
        logger.error(f"😚 Fuck this Baddie: {context.get('message', 'Unknown error')}")

# Catch baddie and use your finger
def fingering(exc_type, exc_value, exc_traceback):
    """Make the baddie feel pleasure"""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.error("🤤 10/10 Baddie found:")
    logger.error(''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)))

# Activate beautiful Baddie catcher ASAP
try:
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(fucking)
    logger.info("🫦 Beautiful Baddie catching mode activated")
except RuntimeError:
    logger.warning("😭 Damn no Baddie will be caught sadly")

# Activate cute baddie catcher immediately
sys.excepthook = fingering
logger.info("🫦 Hardcore Baddie catching mode activated")
