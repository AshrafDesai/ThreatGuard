import os
import pyinotify
from windows_engine import Engine

def RealTime():

    username = os.environ.get('USER')
    usernameUp = username.upper().split(" ")

    ACTIONS = {
        1: "Created",
        2: "Deleted",
        3: "Updated",
        4: "Renamed from something",
        5: "Renamed to something"
    }

    path_to_watch = "/home/" + username
    wm = pyinotify.WatchManager()
    mask = (pyinotify.IN_CREATE |
            pyinotify.IN_DELETE |
            pyinotify.IN_MODIFY |
            pyinotify.IN_MOVED_FROM |
            pyinotify.IN_MOVED_TO)

    class EventHandler(pyinotify.ProcessEvent):
        def process_IN_CREATE(self, event):
            self.handle_event(event)

        def process_IN_DELETE(self, event):
            self.handle_event(event)

        def process_IN_MODIFY(self, event):
            self.handle_event(event)

        def process_IN_MOVED_FROM(self, event):
            self.handle_event(event)

        def process_IN_MOVED_TO(self, event):
            self.handle_event(event)

        def handle_event(self, event):
            paths = [os.path.join(path_to_watch, event.name)]

            if paths[0].startswith("/home/" + username + "/.cache") or \
               paths[0].startswith("/home/" + username + "/.local/share/Trash") or \
               paths[0].startswith("/home/" + username + "/.config") or \
               paths[0].startswith("/home/" + username + "/Downloads") or \
               paths[0].startswith("/home/" + username + "/Desktop"):
                paths.clear()
                return

            try:
                engine.virusScanner(paths[0])
            except:
                pass

            paths.clear()

    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)

    wdd = wm.add_watch(path_to_watch, mask, rec=True)

    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break

RealTime()
##pip install pyinotify
=======
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
    path_to_watch = "/"

    try:
        watch_directory(path_to_watch)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

