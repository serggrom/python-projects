'''

if __name__ == "__main__":
    import multiprocessing as mp
    def washer(dishes, output):
        for dish in dishes:
            print('Washing', dish, 'dish')
            output.put(dish)
    def dryer(input):
        while True:
            dish = input.get()
            print('Drying', dish, 'dish')
            input.task_done()
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()
    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()
'''


import threading

def do_this(what):
    whoami(what)
def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread()
                                  , what))
if __name__ == "__main__":
    whoami("I'm the main programm")
    for n in range(4):
        p = threading.Thread(target=do_this,
        args=("I'm function %s" % n))
        p.start()
























































































































































































































































