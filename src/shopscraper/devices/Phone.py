class Phone:
    def __init__(self, name, color=None, storage=None, memory=None, screen=None, cpu=None, battery=None, os=None, cpu_speed=None, price=None):
        self.name = name
        self.color = color
        self.storage = storage
        self.memory = memory
        self.screen = screen
        self.cpu = cpu
        self.battery = battery
        self.os = os
        self.cpu_speed = cpu_speed
        self.price = price

    def __str__(self):
        return str(
            {
                'name': self.name,
                'color': self.color,
                'storage': self.storage,
                'memory': self.memory,
                'screen': self.screen,
                'cpu': self.cpu,
                'battery': self.battery,
                'os': self.os,
                'cpu_speed': self.cpu_speed,
                'price': self.price
            }
        )