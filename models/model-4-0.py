import math


def reward_function(params):
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']

    distance_modifer = 1e-3

    if params["all_wheels_on_track"] and params["steps"] > 0:
        # reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"] ** 2)
        # check for angle of the track immediatly ahead of the racer

        # Gets the next 2 closest points in front of the racer
        # point1 = waypoints[closest_waypoints[5]]
        # point0 = waypoints[closest_waypoints[0]]
        #
        # track_direction = math.atan2(point1[1] - point0[1], point1[0] - point0[0])
        #
        # track_direction = math.degrees(track_direction)
        #
        # direction_diff = abs(track_direction - heading)
        # if direction_diff > 180:
        #     direction_diff = 360 - direction_diff

        isTurn = 0
        speedModifer = 1e-3
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width
        marker_3 = 0.5 * track_width
        # if angle is high... reward keeping to the inside of the turn
            # Left for left turn
            # Right for right turn
        # if the angle is small or non existant... reward speed and staying in the center
        if (isTurn == 0): #If the track is straight... This should go straight
            if distance_from_center <= marker_1:
                distance_modifer = 2.0
            elif distance_from_center <= marker_2:
                distance_modifer = 1
            elif distance_from_center <= marker_3:
                distance_modifer = 0.1
            else:
                distance_modifer = 1e-3  # likely crashed/ close to off track

        if (speed<1.5 and speed>2):
            speedModifer = 2
        elif (speed>2):
            speedModifer = 4
        else:
            speed = 0.1

        reward = ((params["progress"] / params["steps"]) * 1000) * distance_modifer * speedModifer

    else:
        reward = 1e-3

    return float(reward)