#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Bomb import Bomb
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):  # level1bg images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(3):  # level2bg images number
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Bomb_01':
                return Bomb('Bomb_01', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Bomb_02':
                return Bomb('Bomb_02', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))