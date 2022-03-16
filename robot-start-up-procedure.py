shoulder_motor = robot.getDevice('shoulder_pan_joint')
shoulder_motor.setPosition(1.507)

distance_sensor = robot.getDevice('distance_sensor')
distance_sensor.enable(TIME_STEP)

position_sensor = robot.getDevice('wrist_1_joint_sensor')
position_sensor.enable(TIME_STEP)

for motor in ur_motors:
    motor.setVelocity(speed)
