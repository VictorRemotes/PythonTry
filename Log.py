import datetime
import loguru

loguru.logger.add(
    f'{datetime.date.today():%Y%m%d}.log'
)
#Trace
loguru.logger.trace('<message>')

#Debug
loguru.logger.debug('<message>')

#Info
loguru.logger.info('<message>')

#Success
loguru.logger.success('<message>')

#Warning
loguru.logger.warning('<message>')

#Error
loguru.logger.error('<message>')

#Critical
loguru.logger.critical('<message>')
