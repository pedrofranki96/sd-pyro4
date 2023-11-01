from time import sleep
from threading import Thread
 
# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(2)
    # display a message
    print('This is from another thread')
 
# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread...')
thread.join()
print('Thread finished...')