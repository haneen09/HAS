# device class serves as the base class for all devices in the home automation system.
class Device:
    def __init__(self, device_id, status, device_type, location):
        self.id = device_id
        self.status = status
        self.type = device_type
        self.location = location

    def toggle_status(self):
        self.status = 'ON' if self.status == 'OFF' else 'OFF'

    def update_settings(self, settings):
        pass


class Light(Device):
    def __init__(self, device_id, status, device_type, location, brightness):
        super().__init__(device_id, status, device_type, location)
        self.brightness = brightness

    def adjust_brightness(self, level):
        self.brightness = level

    def update_settings(self, settings):
        if 'brightness' in settings:
            brightness = settings['brightness']
            if 0 <= brightness <= 100:
                self.adjust_brightness(brightness)
            else:
                print(f"Invalid brightness value: {brightness}")


class Thermostat(Device):
    def __init__(self, device_id, status, device_type, location, temperature):
        super().__init__(device_id, status, device_type, location)
        self.temperature = temperature

    def set_temperature(self, temp):
        self.temperature = temp

    def update_settings(self, settings):
        if 'temperature' in settings:
            temp = settings['temperature']
            if 60 <= temp <= 80:
                self.set_temperature(temp)
            else:
                print(f"Invalid temperature value: {temp}")


class Camera(Device):
    def __init__(self, device_id, status, device_type, location, angle):
        super().__init__(device_id, status, device_type, location)
        self.angle = angle

    def adjust_angle(self, new_angle):
        self.angle = new_angle

    def update_settings(self, settings):
        if 'angle' in settings:
            angle = settings['angle']
            if 0 <= angle <= 360:
                self.adjust_angle(angle)
            else:
                print(f"Invalid angle value: {angle}")


# user class represents a user in the home automation system


class User:
    def __init__(self, user_id, name, access_level):
        self.user_id = user_id
        self.name = name
        self.access_level = access_level

    def authenticate(self, credentials):
        # Implement authentication logic here
        return True

    def send_command(self, command, controller):
        # Pass the command to the Controller class
        controller.process_command(self, command)


# scheduler class manages scheduled tasks in the home automation system


class Scheduler:
    def __init__(self):
        self.scheduled_tasks = []

    def add_task(self, task):
        self.scheduled_tasks.append(task)

    def remove_task(self, task_id):
        self.scheduled_tasks = [t for t in self.scheduled_tasks if t.id != task_id]

    def execute_tasks(self):
        # Implement logic to execute scheduled tasks
        pass


class Controller:
    def __init__(self, devices, users):
        self.devices = devices
        self.users = users

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_id):
         self.devices = [d for d in self.devices if d.id != device_id]

    def process_command(self, user, command):
        # Implement logic to process user commands and control devices
        pass


class scheduled_task:
    pass


class Main:
    def __init__(self):
        self.controller = Controller([], [])
    def create_device(self):
        device_type = input("Enter the type of device (Light/Thermostat/Camera): ")
        initial_settings = {}
        if device_type == 'Light':
            initial_settings['brightness'] = int(input("Enter initial brightness: "))
        elif device_type == 'Thermostat':
            initial_settings['temperature'] = float(input("Enter initial temperature: "))
        elif device_type == 'Camera':
            initial_settings['angle'] = int(input("Enter initial angle: "))
        location = input("Enter the location: ")

        if device_type == 'Light':
            device = Light(len(self.controller.devices) + 1, 'OFF', device_type, location, initial_settings['brightness'])
        elif device_type == 'Thermostat':
            device = Thermostat(len(self.controller.devices) + 1, 'OFF', device_type, location, initial_settings['temperature'])
        elif device_type == 'Camera':
            device = Camera(len(self.controller.devices) + 1, 'OFF', device_type, location, initial_settings['angle'])

        self.controller.add_device(device)
        print(f"{device_type} device created with {', '.join(f'{k}={v}' for k, v in initial_settings.items())} in the {location}.")

    def modify_device_settings(self):
        device_id = int(input("Enter the device ID: "))
        device = next((d for d in self.controller.devices if d.id == device_id), None)
        if device:
            settings = {}
            if device.type == 'Light':
                settings['brightness'] = int(input("Enter new brightness: "))
            elif device.type == 'Thermostat':
                settings['temperature'] = float(input("Enter new temperature: "))
            elif device.type == 'Camera':
                settings['angle'] = int(input("Enter new angle: "))
            device.update_settings(settings)
            print(f"{device.type} device {device.id} updated with new settings.")
        else:
            print(f"Device with ID {device_id} not found.")

    def create_user(self):
        name = input("Enter user name: ")
        access_level = input("Enter access level: ")
        user = User(len(self.controller.users) + 1, name, access_level)
        self.controller.users.append(user)
        print(f"User {name} with {access_level} access level created successfully.")

    def user_interaction(self):
        user_id = int(input("Enter your User ID: "))
        user = next((u for u in self.controller.users if u.user_id == user_id), None)
        if user:
            action = input("Enter the action you want to perform (e.g., control a device, modify settings): ")
            if action == 'Control Device':
                device_id = int(input("Enter the device ID: "))
                device = next((d for d in self.controller.devices if d.id == device_id), None)
                if device:
                    settings = {}
                    if device.type == 'Light':
                        settings['brightness'] = int(input("Enter new brightness: "))
                    elif device.type == 'Thermostat':
                        settings['temperature'] = float(input("Enter new temperature: "))
                    elif device.type == 'Camera':
                        settings['angle'] = int(input("Enter new angle: "))
                    device.update_settings(settings)
                    print(f"User {user.name} set the {', '.join(f'{k}={v}' for k, v in settings.items())} of device {device.id}.")
                else:
                    print(f"Device with ID {device_id} not found.")
            else:
                print(f"Action '{action}' is not supported.")
        else:
            print(f"User with ID {user_id} not found.")

    def schedule_event(self):
        event_time = input("Enter the event time (HH:MM AM/PM): ")
        device_id = int(input("Enter the device ID: "))
        device = next((d for d in self.controller.devices if d.id == device_id), None)
        if device:
            action = input(f"Enter the action to perform on the {device.type} device: ")
            if action == 'Set Temperature':
                settings = {'temperature': float(input("Enter the temperature: "))}
            elif action == 'Set Brightness':
                settings = {'brightness': int(input("Enter the brightness: "))}
            elif action == 'Set Angle':
                settings = {'angle': int(input("Enter the angle: "))}
            else:
                print(f"Action '{action}' is not supported.")
                return
            task = scheduled_task(event_time, device, action, settings)
            self.controller.scheduler.add_task(task)
            print(f"Event scheduled at {event_time} to {action} the {device.type} device {device.id}.")
        else:
            print(f"Device with ID {device_id} not found.")

    def run(self):
        while True:
            print("\nHome Automation System Menu:")
            print("1. Create a device")
            print("2. Modify device settings")
            print("3. Create a user")
            print("4. User interaction")
            print("5. Schedule an event")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.create_device()
            elif choice == '2':
                self.modify_device_settings()
            elif choice == '3':
                self.create_user()
            elif choice == '4':
                self.user_interaction()
            elif choice == '5':
                self.schedule_event()
            elif choice == '6':
                print("Exiting Home Automation System...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main = Main()
    main.run()
