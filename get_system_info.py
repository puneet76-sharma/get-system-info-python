import platform

my_system= platform.uname()

system= my_system.system
node_name= my_system.node
release= my_system.release
version= my_system.version
machine= my_system.machine
processor= my_system.processor

print("System: ", system)
print("Node Name: ", node_name)
print("Release: ", release)
print("Version: ", version)
print("Machine: ", machine)
print("Processor: ", processor)

input()