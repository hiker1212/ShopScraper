import csv


def write_to_csv(devices):
    filename = '../../devices.csv'

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "color", "storage", "memory", "screen", "cpu", "battery", "os", "cpu_speed", "price"])
        for device in devices:
            writer.writerow([device.name, device.color, device.storage, device.memory, device.screen, device.cpu, \
                             device.battery, device.os, device.cpu_speed, device.price])
