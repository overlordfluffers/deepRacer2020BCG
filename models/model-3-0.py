def reward_function(params):
    # Setting the weight of each multiplyer
    all_wheels_on = 1.5
    steering_angle = 3

    # Base Reward: Make the car go faster
    reward = (((params["progress"] / params["steps"]) * 100) + (params["speed"] ** 2))

    # Base Modifers
    if params["all_wheels_on_track"]:
        reward = reward * all_wheels_on
    else:
        reward = 1e-3
    if abs(params["steering_angle"]) < 5:
        reward = reward * steering_angle

    return float(reward)