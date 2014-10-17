from datetime import datetime
file_log = open('C:\\important\\%s.txt' % datetime.now().strftime('%m%d%Y%H%M%S'), 'w+')