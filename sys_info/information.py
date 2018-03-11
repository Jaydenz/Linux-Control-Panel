
import psutil, platform, json, datetime, time

def taskmanage():
    all_process = []
    pid = [8528,7512]#psutil.pids()
    for i in pid:
        process = []
        p = psutil.Process(i)
        system_time = time.time()
        running_time = p.create_time()
        total_time = round((system_time - running_time) / 60, 1)

        process.append(p.pid)
        process.append(p.name())
        process.append(p.status())
        process.append(p.cpu_percent())
        process.append(round(p.memory_info().rss / 1048576, 1))
        process.append(total_time)
        process.append(p.exe())

        #process.append(p.io_counters())

        all_process.append(process)
    return all_process
#print(taskmanage())

def get_cpu_percent():
    return psutil.cpu_percent()


def system_release():
    bit = platform.architecture()[0]
    type = platform.system()
    release = platform.platform()
    node_name = platform.node()
    platform.dist()


def hardware_info():
    physics_cpu_core =  psutil.cpu_count(logical=False)
    logic_cpu_core = psutil.cpu_count(logical = True)


    def cpu_info():
        pass

def user_info():
    curr_login_user = psutil.users()

def software():
    py_version = platform.python_version()
    achieve_py = platform.python_implementation()



'''
class System_Information(object):

    def __init__(self, mem, cpu):
        self.mem = mem
        self.cpu = cpu

    def ge(self):
        print('%s: %s' % (self.mem, self.cpu))



mem = System_Information(psutil.virtual_memory().percent, psutil.cpu_percent())
#lisa = Student('Lisa Simpson', 87)
print(mem.cpu)
'''