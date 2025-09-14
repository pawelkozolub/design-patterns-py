from widget import Widget

class Dialog(Widget):
    @staticmethod
    def handle_ok(event):
        print(f"Dialog - accepted by event: {event.name}")
    
    @staticmethod
    def handle_cancel(event):
        print(f"Dialog - cancelled by event: {event.name}")
    
    @staticmethod
    def handle_send(event):
        print(f"Dialog - sent by event: {event.name}")