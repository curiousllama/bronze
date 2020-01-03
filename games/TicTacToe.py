#!/usr/bin/env python
# coding: utf-8

# Tic-tac-toe
# We will use gym.
# Let's try to use MVC.

# In[91]:


import gym
from gym import spaces
import numpy as np

class Game:
    """Custom Environment that follows gym interface"""
    # We will add a non-default method legal_actions.""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(TicTacToe, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
#         The actions are simply each square.
        self.action_space = spaces.Discrete(9)
        # The observations will just be the board and then an indicator for the turn.
        # 0 is empty, 1 is X, 2 is O.
        # For the turn indicator, 0 is X, 1 is O.
        
        self.observation_space = spaces.MultiDiscrete((3,3,3,3,3,3,3,3,3,2))
        self.board = np.array([0]*9)
        self.turn = "X"
        self.outcome = -1 #ongoing

    def _update_outcome(self):
        if self.outcome != -1:
            raise error
        
        #Horiz player 1
        for i in range(2):
            if (self.board[3*i] == 1 and self.board[1+3*i] == 1 and self.board[2+3*i] == 1):
                self.outcome = 1 #First Player won.
        #Vert player 1
        for i in range(2):
            if (self.board[i] == 1 and self.board[3+i] == 1 and self.board[6+i] == 1):
                self.outcome = 1 #First Player won.
        
        #Diag player 1
        if (self.board[0] == 1 and self.board[4] == 1 and self.board[8] == 1):
                self.outcome = 1
        
        if (self.board[2] == 1 and self.board[4] == 1 and self.board[6] == 1):
                self.outcome = 1
        
        
        #Horiz player 2
        for i in range(2):
            if (self.board[3*i] == 2 and self.board[1+3*i] == 2 and self.board[2+3*i] == 2):
                self.outcome = 2 #First Player won.
        #Vert player 2
        for i in range(2):
            if (self.board[i] == 2 and self.board[3+i] == 2 and self.board[6+i] == 2):
                self.outcome = 2 #First Player won.
        
        #Diag player 2
        if (self.board[0] == 2 and self.board[4] == 2 and self.board[8] == 2):
                self.outcome = 2
        
        if (self.board[2] == 2 and self.board[4] == 2 and self.board[6] == 2):
                self.outcome = 2
        
        if self.outcome not in (1,2):
            if 0 not in self.board:
                self.outcome = 0
    
    def _set_turn(self, new_turn):
        self.turn = new_turn
    
    def _change_turn(self):
        if self.turn == "X":
            self._set_turn("O")
        else:
            self._set_turn("X")
    
    def _set_board(self, new_board):
        self.board = new_board
    
    
    def check_action_legal(self, action):
        if action not in self.action_space:
            return False
        if self.board[action] != 0:
            return False
        return True
    
    def legal_actions(self):
        # Simply returns a list of actions that are legal.
        legal_action_list = []
        for action in range(0,self.action_space.n):
            if self.check_action_legal(action):
                legal_action_list.append(action)
        return legal_action_list
            
    
    def step(self, action):
    # Execute one time step within the environment
    # Needs to return observation, done, reward, info.
        if not self.check_action_legal(action):
            raise exception
        
        old_board = self.board
        new_board = old_board
        if self.turn == "X":
            new_board[action] = 1
            self._set_board(new_board)
        if self.turn == "O":
            new_board[action] = 2
        self._set_board(new_board)
        self._update_outcome()
    #             self._update_state()
        self._change_turn()
        
        if self.turn == "X":
            observation = np.append(self.board,[0])
        else:
            observation = np.append(self.board,[1])
        
        if self.outcome in (1,2,3):
            done = 1
        else:
            done = 0
        
        if self.outcome == 1:
            reward = 1
        
        elif self.outcome == 2:
            reward = -1
        
        else:
            reward = 0
        
        return observation, reward, done, _
    
    def reset(self):
    # Reset the state of the environment to an initial state
        self.board = np.array([0]*9)
        self.turn = "X"
        self.outcome = -1 #ongoing
    
    def render(self, mode='human', close=False):
    # Render the environment to the screen
        #Assumes correct input.
        board = self.board
        display_board=[' ']*9
        for i in range(9):
            if board[i] == 1:
                display_board[i] = "X"
            if board[i] == 2:
                display_board[i] = "O"
        print(display_board[0] + '|' + display_board[1] + '|' + display_board[2])
        print('-'*5)
        print(display_board[3] + '|' + display_board[4] + '|' + display_board[5])
        print('-'*5)
        print(display_board[6] + '|' + display_board[7] + '|' + display_board[8])
        turn = self.turn
        if turn == "X":
            print("It's X's turn.")
        if turn == "O":
            print("It's O's turn.")
        outcome = self.outcome
        if outcome == -1:
            print("The game is ongoing.")
        if outcome == 1:
            print("Player X won.")
        if outcome == 2:
            print("Player O won.")
        if outcome == 3:
            print("The game was a draw.")
        input("Press enter to take a step ")

    def get_move(self):
        while True:
            square_in = input('Enter square: ')
            if square_in not in ('1','2','3','4','5','6','7','8','9'):
                print("Not an appropriate choice.")
            else:
                square = int(square_in) - 1
                action = square
                if self.check_action_legal(action):
                    break
                else:
                    print("Not a valid move.")
        return action

    def close(self):
        """Properly close the game.
        """
        self.env.close()

