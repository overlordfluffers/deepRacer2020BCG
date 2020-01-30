import math


def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    #Editable Parameter to Tweak
    DIRECTION_THRESHOLD = 10.0


    # Read input parameters
    wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    if wheels_on_track:
        # Calculate 3 markers that are at varying distances away from the center line
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width
        marker_3 = 0.5 * track_width

        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            reward = 5
        elif distance_from_center <= marker_2:
            reward = 1
        elif distance_from_center <= marker_3:
            reward = 0.1
        else:
            reward = 1e-3  # likely crashed/ close to off track
    else:
        reward = 1e-3

    point1 = waypoints[closest_waypoints[1]]
    point0 = waypoints[closest_waypoints[0]]

    track_direction = math.atan2(point1[1] - point0[1], point1[0] - point0[0])

    track_direction = math.degrees(track_direction)

    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    print('============================= Point 0:  ', point0)
    print('============================= Point 1:  ', point1)

    return float(reward)
