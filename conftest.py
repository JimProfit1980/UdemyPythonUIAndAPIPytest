import os
import time

# Let Playwright's API client (bundled Node) trust the Windows certificate store,
# so API calls work behind networks that inspect HTTPS traffic.
os.environ.setdefault("NODE_USE_SYSTEM_CA", "1")

# import pyodbc
#
# print(pyodbc.drivers())
#
# time.sleep(3)
