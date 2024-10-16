# This program calculates some aircraft performance metrics.

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hr = fuel_capacity/fuel_consumption_rate
    return endurance_in_hr

def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    hours = fuel_capacity/fuel_consumption_rate
    return hours*true_air_speed

def calculate_total_weight(payload, fuel_weight):
    return dry_weight + payload + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    total_moment = sum(moment_list)
    return total_moment/total_weight

def calculate_moment(weight, arm):
    return weight*arm

def calculate_lift(cl, rho, v, s):
    return 0.5*cl*rho*v*v*s

def calculate_drag(cd, rho, v, s):
    return 0.5*cd*rho*v*v*s

def calculate_weight(mass, g):
    return mass*g

def calculate_acceleration(thrust, drag, weight, mass):
    return (thrust-drag-weight)/mass

def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration*time

def calculate_distance(velocity, time):
    return velocity*time
def pretty_print(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    print("Performance Calculations:")
    print(f"Range: {range:.2f} km")
    print(f"Endurance: {endurance:.2f} hr")
    print(f"Total Weight: {total_weight} kg")
    print(f"Center of Gravity Position: {cg_position:.2f} m")
    print(f"Lift: {lift:.0f} N")
    print(f"Drag: {drag:.0f} N")
    print(f"Weight: {weight:.0f} N")
    print(f"Acceleration: {acceleration:.1f} m/s^2")
    print(f"Velocity: {velocity:.1f} m/s")
    print(f"Distance: {distance:.1f} m")

def save_info_to_file(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file):
    file.write("Performance Calculations:\n")
    file.write(f"Range: {range:.2f} km\n")
    file.write(f"Endurance: {endurance:.2f} hr\n")
    file.write(f"Total Weight: {total_weight} kg\n")
    file.write(f"Center of Gravity Position: {cg_position:.2f} m\n")
    file.write(f"Lift: {lift:.0f} N\n")
    file.write(f"Drag: {drag:.0f} N\n")
    file.write(f"Weight: {weight:.0f} N\n")
    file.write(f"Acceleration: {acceleration:.1f} m/s^2\n")
    file.write(f"Velocity: {velocity:.1f} m/s\n")
    file.write(f"Distance: {distance:.1f} m")
    file.close()


# INPUTS
fuel_capacity = 3785             # [kg]
fuel_consumption_rate = 190      # [kg/hr]
true_air_speed = 150             # Air speed [knots]
payload = 2268                   # Payload weight [kg]
fuel_weight = 2722               # Fuel weight [kg]
moment_list = [13560, 3390]      # Moments [N*m]
dry_weight = 700                 # Aircraft dry weight [kg]
CL = 1.5                         # Lift coefficient
rho = 1.225                      # Air density in [kg/m^3]
v = 100                          # Aircraft velocity [m/s]
S = 20                           # Wing area [m^2]
CD = 0.02                        # Drag coefficient
mass = 5000                      # Mass [kg]
g = 9.81                         # Gravitational acceleration [m/s^2]
thrust = 6000                    # [N]
v_0 = 50                         # Initial velocity [m/s]
time = 10                        # Time [s]

# CALCULATIONS
range = calculate_range(fuel_capacity,fuel_consumption_rate,true_air_speed)
endurance = calculate_endurance(fuel_capacity,fuel_consumption_rate)
tot_weight = calculate_total_weight(payload,fuel_weight)
cg_position = calculate_cg_position(moment_list,tot_weight)
lift = calculate_lift(CL,rho,v,S)
drag = calculate_drag(CD,rho,v,S)
weight = calculate_weight(mass,g)
acc = calculate_acceleration(thrust,drag,weight,mass)
velocity = calculate_velocity(v_0,acc,time)
distance = calculate_distance(velocity,time)

pretty_print(range, endurance, tot_weight, cg_position, lift, drag, weight, acc, velocity, distance)

# SAVE PERFORMANCE VALUES INTO A FILE
with open("Aircraft Performance.txt", "w") as f:
    save_info_to_file(range, endurance, tot_weight, cg_position, lift, drag, weight, acc, velocity, distance, f)