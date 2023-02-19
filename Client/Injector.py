import psutil
import subprocess
import time
import frida
import sys

class MacOSX:
    def __init__(self):
        self.PROCESS_NAME = "Archero"
        self.SCRIPT_NAME = "agent.js"
        self.PATH_NAME = r"/Users/martinjakobsson/Library/Containers/io.playcover.PlayCover/Archero.app"
        
    def start(self):
        while True:
            time.sleep(0.3)
            if self.check_if_process_running():
                self.kill_process()
                print(f'[+]: {self.PROCESS_NAME} was killed.')
                self.start_process()
                print(f'[!]: {self.PROCESS_NAME} was started.')
            else:
                self.start_process()
                print(f'[+] {self.PROCESS_NAME} was started.')

            # Wait for the process to start
            while not self.check_if_process_running():
                time.sleep(0.3)

            # Run the command
            subprocess.call(["reset"])
            subprocess.run(["sudo", "frida", "-l", self.SCRIPT_NAME,
                        self.PROCESS_NAME])
    
    def check_if_process_running(self):
        for process in psutil.process_iter():
            try:
                if self.PROCESS_NAME.lower() in process.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False


    def start_process(self):
        subprocess.call(["sudo", "open", self.PATH_NAME])


    def kill_process(self):
        for process in psutil.process_iter():
            try:
                if self.PROCESS_NAME.lower() in process.name().lower():
                    process.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
class iOS:
    def __init__(self):
        self.CONNECTED_TO_PHONE = False
        self.ATTACHED_TO_PROCESS = False
        self.PROCESS_FOUND = False
        
        self.PROCESS_NAME = "Archero"
        self.BUNDLE_NAME = "com.habby.archero.3Z58P8MNX4"
        self.SCRIPT_NAME = "agent.js"
    
    def killProcess(self):
        try:
            subprocess.run(["sudo", "frida-kill", "-U", self.PROCESS_NAME])
            print(f'[+]: Process killed')
            return True
        except subprocess.CalledProcessError as e:
            print(f'[-]: Process not killed, error: {e}')
            return False
    
    # Do not kill process, only attach to already running process.
    def injectScript(self):
        try:
            subprocess.run(["sudo", "frida", "-U", "-l", "agent.js"])
            print(f'[+]: Script injected')
            return True
        except subprocess.CalledProcessError as e:
            print(f'[-]: Script not injected, error: {e}')
            return False
    
    # Do not kill process, only attach to already running process.
    def startAndinject(self):
        try:
            subprocess.run(["sudo", "frida", "-U", "-l", "agent.js", "-f",
                           "com.habby.archero.3Z58P8MNX4"])
            print(f'[+]: Process started and script injected')
            return True
        except subprocess.CalledProcessError as e:
            print(f'[-]: Process not started and script not injected, error: {e}')
            return False

    def awaitProcess(self):
        while self.PROCESS_FOUND == False:
            time.sleep(1)
            processes = device.enumerate_processes()
            for process in processes:
                if process.name == "Archero":
                    print("[+]: Archero found")
                    return
            else:
                print("[-]: Archero not found, waiting...")
     
    
    def start(self):
        #self.startAndinject()
        subprocess.run(["sudo", "frida", "-U", "-l", "agent.js", "-f",
                        "com.habby.archero.3Z58P8MNX4"])
        print(f'[+]: Process started and script injected')   
class Android:
    def __init__(self):
        self.CONNECTED_TO_PHONE = False
        self.ATTACHED_TO_PROCESS = False
        self.PROCESS_FOUND = False
        
        self.PROCESS_NAME = "Archero"
        self.BUNDLE_NAME = "com.habby.archero"
        self.SCRIPT_NAME = "agent_android.js"
        
    def killProcess(self):
        try:
            subprocess.run(["sudo", "frida-kill", "-U", self.PROCESS_NAME])
            print(f'[+]: Process killed')
            return True
        except subprocess.CalledProcessError as e:
            print(f'[-]: Process not killed, error: {e}')
            return False

    # Do not kill process, only attach to already running process.
    def injectScript(self):
        try:
            subprocess.run(["sudo", "frida", "-U", "-l", "agent_android.js"])
            print(f'[+]: Script injected')
            return True
        except subprocess.CalledProcessError as e:
            print(f'[-]: Script not injected, error: {e}')
            return False

    # Do not kill process, only attach to already running process.
    def startAndinject(self):
        try:
            subprocess.run(["sudo", "frida", "-U", "-l", "agent_android.js", "-f",
                           "com.habby.archero"])
            print(f'[+]: Process started and script injected')
            return True
        except subprocess.CalledProcessError as e:
            print(
                f'[-]: Process not started and script not injected, error: {e}')
            return False

    def awaitProcess(self):
        while self.PROCESS_FOUND == False:
            time.sleep(1)
            processes = device.enumerate_processes()
            for process in processes:
                if process.name == "Archero":
                    print("[+]: Archero found")
                    return
            else:
                print("[-]: Archero not found, waiting...")

    def start(self):
        # self.startAndinject()
        subprocess.run(["sudo", "frida", "-U", "-l", "agent_android.js", "-f",
                        "com.habby.archero"])
        print(f'[+]: Process started and script injected')

    

IS_ANDROID = 1  
IS_IOS = 0
IS_MACOSX = 0 

def my_message_handler(message, payload):
    print(message)


if __name__ == "__main__":
    
    if IS_ANDROID:
        android = Android()
        android.start()
    elif IS_IOS:
        ios = iOS()
        ios.start()
    elif IS_MACOSX:
        computer = Computer()
        computer.start()

    # jscode = open("agent_android.js").read()
    # device = frida.get_device("emulator-5554")
    # processId = device.spawn('com.habby.archero')
    # session = device.attach(processId)
    # time.sleep(2)
    # script = session.create_script(jscode)
    # script.on("message", my_message_handler)
    # script.load()
    
    # print('[*]: Attched to Archero process')
    # command = ""
    # while True:
    #     command = input(
    #         "Enter command:\n1: Exit\n2: Call secret function\n3: Hook Secret\nchoice:")
    #     if command == "1":
    #         break
    #     elif command == "2":
    #         script.exports.callsecretfunction()
    #     elif command2 == "3":
    #         script.exports.hooksecretfunction()