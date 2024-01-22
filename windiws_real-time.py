import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from windows_engine import Engine 

class RealTimeHandler(FileSystemEventHandler):
    def __init__(self, engine_instance):
        self.engine_instance = engine_instance

    def on_any_event(self, event):
        if event.is_directory:
            return

        file_path = os.path.abspath(event.src_path)

        # Add your path filtering conditions here
        if file_path.startswith("C:\\Users\\{}\\AppData\\".format(os.environ.get('USERNAME'))):
            return
        # Add more conditions based on your requirements

        try:
            self.engine_instance.virusScanner(file_path)  # Use the virusScanner method from the Engine
        except Exception as e:
            print(f"Error scanning file {file_path}: {e}")

def real_time_monitor(path_to_watch):
    engine_instance = Engine("md5")  # Create an instance of the Engine
    event_handler = RealTimeHandler(engine_instance)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    real_time_monitor("D:\\")
