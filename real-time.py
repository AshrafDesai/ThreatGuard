import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import engine


logging.basicConfig(level=logging.INFO)


engine_instance = engine.Engine("md5") 

class VirusScanner(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            logging.info(f"Folder created: {event.src_path}")
        else:
            logging.info(f"File created: {event.src_path}")
            # Scan the file for viruses
            result = engine_instance.quick_scan(event.src_path, [".jpg", ".png", ".pdf", ".ppt"])
            if result[1]:
                logging.warning("Virus found in file: {}".format(event.src_path))
                
            else:
                logging.info("File is clean.")

    def on_deleted(self, event):
        if event.is_directory:
            logging.info(f"Folder deleted: {event.src_path}")
        else:
            logging.info(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            logging.info(f"Folder modified: {event.src_path}")
        else:
            logging.info(f"File modified: {event.src_path}")
           

    def on_moved(self, event):
        if event.is_directory:
            logging.info(f"Folder moved: {event.src_path} to {event.dest_path}")
        else:
            logging.info(f"File moved: {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
    
    directory_to_watch = r"C:\Ashraf"  

   
    observer = Observer()
    observer.schedule(VirusScanner(), directory_to_watch, recursive=True)
    observer.start()

    try:
        while observer.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()  # Wait for the observer to stop
        
