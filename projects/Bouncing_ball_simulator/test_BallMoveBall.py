# ********RoostGPT********
"""
Test generated by RoostGPT for test python-unit-testing-2 using AI Type  and AI Model 

ROOST_METHOD_HASH=move_ball_fdd06019e1
ROOST_METHOD_SIG_HASH=move_ball_783a83baa3


Scenario 1: Validating the velocity change and position after moving the ball
Details:
  TestName: test_move_ball_velocity_and_position
  Description: This test verifies that the velocity of the ball and its position changes correctly when the move_ball function is invoked.
Execution:
  Arrange: Initialize an object of the class and note down the initial X, Y, velocityX, and velocityY values.
  Act: Call the move_ball function on the object.
  Assert: Check if the new X, Y, velocityX, and velocityY values are as expected based on the function's logic.
Validation:
  Rationalize the importance of the test: This test is crucial as it validates the core functionality of the move_ball function, which is to update the velocity and the position of the ball.

Scenario 2: Validating the ball's collision with the walls
Details:
  TestName: test_move_ball_collision
  Description: This test verifies that when the ball hits the walls, the velocity changes direction and the ball's position is set correctly.
Execution:
  Arrange: Initialize an object of the class with X and Y values such that the ball is at one of the walls.
  Act: Call the move_ball function on the object.
  Assert: Check if the velocity has changed direction and the ball's position is set correctly.
Validation:
  Rationalize the importance of the test: This test is important as it validates the boundary conditions of the move_ball function, ensuring that the ball's movement is constrained within the given dimensions.
"""

# ********RoostGPT********
import pytest
import pygame, time, random
from Bouncing_ball_simulator.ball_bounce import ball

class Test_BallMoveBall:

    @pytest.mark.regression
    def test_move_ball_velocity_and_position(self):
        # arrange
        ball_obj = ball()
        initial_X = ball_obj.X
        initial_Y = ball_obj.Y
        initial_velocity_X = ball_obj.velocityX
        initial_velocity_Y = ball_obj.velocityY

        # act
        ball_obj.move_ball()

        # assert
        assert ball_obj.velocityY == initial_velocity_Y + ball.g
        assert ball_obj.X == initial_X + initial_velocity_X
        assert ball_obj.Y == initial_Y + ball_obj.velocityY

    @pytest.mark.regression
    def test_move_ball_collision(self):
        # arrange
        ball_obj = ball()
        ball_obj.X = 768
        ball_obj.Y = 0
        initial_velocity_X = ball_obj.velocityX
        initial_velocity_Y = ball_obj.velocityY

        # act
        ball_obj.move_ball()

        # assert
        assert ball_obj.velocityX == -initial_velocity_X
        assert ball_obj.velocityY == -initial_velocity_Y
        assert ball_obj.Y == 0
        assert ball_obj.X == 768
