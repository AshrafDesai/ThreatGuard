import os
import time
import struct
from inotify_simple import INotify
import linux_engine

def watch_directory(path):
    inotify = INotify()

    # Watch for create, delete, modify, move events
    watch_flags = (INotify.CLOSE_WRITE | INotify.DELETE | INotify.MODIFY | INotify.MOVE | INotify.MOVED_FROM)

    watch = inotify.add_watch(path.encode(), watch_flags)

    try:
        while True:
            for event in inotify.read():
                handle_event(path, event)

    except KeyboardInterrupt:
        pass
    finally:
        inotify.rm_watch(watch)

def handle_event(path, event):
    event_type = event.mask

    if event_type & INotify.IN_CREATE or event_type & INotify.IN_MOVED_TO:
        full_path = os.path.join(path, event.name.decode())
        print(f"File Created: {full_path}")
        try:
            linux_engine.virusScanner(full_path)
        except Exception as e:
            print(f"Error scanning file: {e}")

    elif event_type & INotify.IN_DELETE or event_type & INotify.IN_MOVED_FROM:
        full_path = os.path.join(path, event.name.decode())
        print(f"File Deleted: {full_path}")

    elif event_type & INotify.IN_MODIFY:
        full_path = os.path.join(path, event.name.decode())
        print(f"File Modified: {full_path}")
        try:
            linux_engine.virusScanner(full_path)
        except Exception as e:
            print(f"Error scanning file: {e}")

if __name__ == "__main__":
    path_to_watch = "/home/ashraf/"

    try:
        watch_directory(path_to_watch)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
