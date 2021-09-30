def reward_function(params):
    # Editable Parameter to Tweak
    DIRECTION_THRESHOLD = 10.0
    STEERING_THRESHOLD = 5.0
    SPEED_THRESHOLD = 1.5
    SPEED_MAX = 3.0

    # Read input parameters
    wheels_on_track = params['all_wheels_on_track']
    is_offtrack = params['is_offtrack']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']

    # Break glass if car is driving bad
    if not wheels_on_track or is_offtrack:
        reward = 1e-3
        return float(reward)

    # Quadratic sub-reward to allow for minor deviations from centerline
    reward = 1 - (distance_from_center / (track_width / 2)) ** 2

    # Reward small amounts of steering input and high speeds
    if abs(steering_angle) < STEERING_THRESHOLD and speed > SPEED_THRESHOLD:
        reward += speed / SPEED_MAX

    # Reward a small amount of steps needed to get around a track
    reward += progress / steps

    return reward
