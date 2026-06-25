class CombatDrone :

    def __init__(self,name,battery):
        self._name = name
        self.set_battery(battery)

    def get_name(self):
        return self._name
    
    def get_battery(self):
        return self._battery
    
    def set_battery(self,new_level):
        if new_level >=0 and new_level <=100:
            self._battery = new_level
        else:
            self._battery = 0
            print("SYSTEM ERROR: Telemetry breach. Battery must be between 0 and 100")
    
    def scan_target(self):
        print(f"Drone {self.get_name()} is scanning. Battery level :{self.get_battery()} ")


class SniperDrone(CombatDrone):

    def __init__(self, name, battery,laser_range):
        super().__init__(name,battery)
        self._laser_range = laser_range
       
    def get_laser_range(self):
        return self._laser_range
    
if __name__ == "__main__" :
    sniper_one = SniperDrone("Ghost-01",67,1500)
    sniper_one.scan_target()
    print(sniper_one.get_laser_range())
    
