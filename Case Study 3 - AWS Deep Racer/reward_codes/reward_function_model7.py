import math

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    progress = params['progress']
    is_offtrack=params['is_offtrack']
    
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 600

    # Initialize the reward with typical value
    reward = 1.0

    # Set the speed threshold based your action space
    SPEED_THRESHOLD = 1.5

    #Get reward if completes the lap
    if progress == 100:
        reward += 100
    elif is_offtrack:
        reward-=50

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5
    
    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0
    
    # Calculate 5 markers that are at varying distances away from the center line
    marker_1 = 0.01 * track_width
    marker_2 = 0.1 * track_width
    marker_3 = 0.2 * track_width
    marker_4 = 0.3 * track_width
    marker_5 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if all_wheels_on_track and distance_from_center <= marker_1:
        reward = 1.0
    elif all_wheels_on_track and distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.2
    elif distance_from_center <= marker_4:
        reward = 0.1
    elif distance_from_center <= marker_5:
        reward = 0.001
    else:
        reward = 1e-3  # likely crashed/ close to off track
        
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15 

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # Penalize reward if the car goes too slow
    if speed < SPEED_THRESHOLD:
        reward *= 0.8
    
    return float(reward)

