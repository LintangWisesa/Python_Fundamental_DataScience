
# do once per sec

import threading

def printit():
  threading.Timer(1.0, printit).start()
  print("Hello, World!")

printit()
