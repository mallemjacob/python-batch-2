class MobilePhones:
    def __init__(self, display, camera, chipset, battery):
        self.display_size = display
        self.camera_pixels = camera
        self.chipset_model = chipset
        self.battery_capacity = battery

    def calling(self):
        print("calling....")
    
    def texting(self):
        print("Texting...")

apple_iphone_17 = MobilePhones(6.3, 48, 'A19', 3692)

print("This model " + apple_iphone_17.chipset_model + " has display size of " + str(apple_iphone_17.display_size))

apple_iphone_17.calling()