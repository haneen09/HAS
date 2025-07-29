import unittest
from HAS import Device, Light, Thermostat, Camera, User, Scheduler, Controller, scheduled_task

class TestHomeAutomationSystem(unittest.TestCase):
    def setUp(self):
        # Initialize test objects
        self.light = Light(1, 'OFF', 'Light', 'Living Room', 50)
        self.thermostat = Thermostat(2, 'OFF', 'Thermostat', 'Bedroom', 70)
        self.camera = Camera(3, 'OFF', 'Camera', 'Backyard', 180)
        self.user = User(1, 'Test User', 1)
        self.scheduler = Scheduler()
        self.controller = Controller([], [self.user])

    def test_device_toggle_status(self):
        self.light.toggle_status()
        self.assertEqual(self.light.status, 'ON')

    def test_light_adjust_brightness(self):
        self.light.adjust_brightness(75)
        self.assertEqual(self.light.brightness, 75)

    def test_thermostat_set_temperature(self):
        self.thermostat.set_temperature(65)
        self.assertEqual(self.thermostat.temperature, 65)

    def test_camera_adjust_angle(self):
        self.camera.adjust_angle(270)
        self.assertEqual(self.camera.angle, 270)

    def test_user_authentication(self):
        credentials = {'username': 'Test User', 'password': 'test_password'}
        self.assertTrue(self.user.authenticate(credentials))

    def test_scheduler_add_remove_task(self):
        task = scheduled_task('12:00 PM', self.light, 'Set Brightness', {'brightness': 80})
        self.scheduler.add_task(task)
        self.assertEqual(len(self.scheduler.scheduled_tasks), 1)
        self.scheduler.remove_task(task.id)
        self.assertEqual(len(self.scheduler.scheduled_tasks), 0)

    def test_controller_add_remove_device(self):
        self.controller.add_device(self.light)
        self.assertEqual(len(self.controller.devices), 1)
        self.controller.remove_device(self.light.id)
        self.assertEqual(len(self.controller.devices), 0)


if __name__ == '__main__':
    unittest.main()
