class Car():
    def __init__(self,colour,max_speed,acceleration,tyre_friction,current_speed):
        self.colour=colour
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.current_speed=current_speed
    def start_engine(self):
        self.start_engine=True
    def stop_engine(self):
        self.start_engine=False
    def apply_brakes(self):
        if self.current_speed>=self.tyre_friction:
            self.current_speed=self.current_speed-self.tyre_friction
        else:
            self.current_speed=0
        print(self.current_speed)
    def sound_horn(self):
        if self.start_engine==True:
            print("Beep Beep")
        else:
            print("Car has not started yet")
s1=Car("black","120RPM","90kmph",58,79)
s1.start_engine()
s1.sound_horn()
s1.apply_brakes()
s1.stop_engine()
s1.apply_brakes()
