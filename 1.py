class Star_Cinema:
    hall_list = []
    
    @classmethod
    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self):
        pass
        