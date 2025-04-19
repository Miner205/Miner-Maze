import pygame
from random import randint
from room import Room, get_walls
# from items import Key
from minimap import Minimap


class Maze:
    def __init__(self, difficulty, player):

        self.difficulty = difficulty   # easy, medium or hard
        if self.difficulty == "easy":
            self.size = 2*randint(1, 2)+1
        elif self.difficulty == "hard":
            self.size = 2*randint(3, 4)+1
        else:
            self.size = 2*randint(2, 3)+1
        self.rooms = generate_rooms(self.size, player)
        self.all_walls = []
        for row in range(self.size):
            for col in range(self.size):
                self.all_walls.append(self.rooms[row][col].walls)

        self.minimap = Minimap()

        self.visible_rooms = []
        self.update_rooms_visibility(player)

        self.maze_ended = False

    def update_rooms_visibility(self, player):
        nearby_rooms = []
        player_room = None
        for row in range(max(0, player.position[1]+self.size//2-player.vision_range-1), min(player.position[1]+self.size//2+player.vision_range+2, self.size)):
            for col in range(max(0, player.position[0]+self.size//2-player.vision_range-1), min(player.position[0]+self.size//2+player.vision_range+2, self.size)):
                # nearby rooms = rooms that are near the player :
                self.rooms[row][col].nearby = abs(self.rooms[row][col].position[0]-player.position[0])+abs(self.rooms[row][col].position[1]-player.position[1]) <= player.vision_range
                if self.rooms[row][col].nearby:
                    nearby_rooms.append(self.rooms[row][col])
                # explored rooms = rooms that have been visited by the player :
                if self.rooms[row][col].position == player.position:
                    self.rooms[row][col].explored = True
                    player_room = self.rooms[row][col]
                if self.rooms[row][col] not in self.minimap.explored_rooms and self.rooms[row][col].explored:
                    self.minimap.explored_rooms.append(self.rooms[row][col])
        # visible rooms = rooms that the player can see : near the player + path to the player
        self.visible_rooms = []
        for room in nearby_rooms:
            room.visible = self.does_path_exist(nearby_rooms, room, player_room)
            if room.visible:
                self.visible_rooms.append(room)

    def update(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            ...
            # if player on a tp, tp the player
            # if player on a end, self.maze_ended = True

    def print(self, screen):
        for room in self.visible_rooms:
            room.print(screen)

    def does_path_exist(self, sample, room_a, room_b):
        """return if there is a path between two rooms in a sample of rooms/the maze or not.
        don't include paths with teleportation."""
        if room_a not in sample or room_b not in sample:
            return False
        if room_a == room_b:
            return True
        room_to_check = [room_a]
        room_already_check = []
        while room_to_check:
            for r_d in [self.get_west_room(room_to_check[0]), self.get_south_room(room_to_check[0]), self.get_east_room(room_to_check[0]), self.get_north_room(room_to_check[0])]:
                r = r_d
                if r in sample and r not in room_already_check:
                    if r == room_b:
                        return True
                    else:
                        room_to_check.append(r)
            room_already_check.append(room_to_check.pop(0))
        # if no path :
        return False

    def does_path_exist_for_rooms_visibility(self, sample, room_a, room_b):
        """ slightly modified version of does_path_exist to be more efficient here.
        return if there is a path between two rooms in a sample of rooms/the maze or not.
        don't include paths with teleportation."""
        ...

        # bug visibility to fix : si cul de sac visibilty doesn't work

        # if neighbor in self.visible_rooms

    def get_west_room(self, room):
        """return the room to the west of the room given in parameter
        if there is a door to the west and the room to the west exist,
        else return None."""
        if room.number[0] == '1' and room.position[0]+(self.size//2) != 0:
            return self.rooms[room.position[1]+(self.size//2)][room.position[0]+(self.size//2)-1]
        return None

    def get_south_room(self, room):
        """return the room to the south of the room given in parameter
        if there is a door to the south and the room to the south exist,
        else return None."""
        if room.number[1] == '1' and room.position[1]+(self.size//2) != self.size-1:
            return self.rooms[room.position[1]+(self.size//2)+1][room.position[0]+(self.size//2)]
        return None

    def get_east_room(self, room):
        """return the room to the east of the room given in parameter
        if there is a door to the east and the room to the east exist,
        else return None."""
        if room.number[2] == '1' and room.position[0]+(self.size//2) != self.size-1:
            return self.rooms[room.position[1]+(self.size//2)][room.position[0]+(self.size//2)+1]
        return None

    def get_north_room(self, room):
        """return the room to the north of the room given in parameter
        if there is a door to the north and the room to the north exist,
        else return None."""
        if room.number[3] == '1' and room.position[1]+(self.size//2) != 0:
            return self.rooms[room.position[1]+(self.size//2)-1][room.position[0]+(self.size//2)]
        return None

def generate_rooms(size, player):
    rooms = [[Room(player.rect.x+player.rect.w//2, player.rect.y+player.rect.h//2) for _ in range(size)] for _ in range(size)]
    rooms[size // 2][size // 2] = Room(player.rect.x+player.rect.w//2, player.rect.y+player.rect.h//2, True, "1111", "start")
    for row in range(size):
        for col in range(size):
            criteria = rooms[row][col].number

            if row == 0:   # borders of maze are walls :
                criteria = new_number(criteria, "0000", 'south')
            if row == size-1:
                criteria = new_number(criteria, "0000", 'north')
            if col == 0:
                criteria = new_number(criteria, "0000", 'east')
            if col == size-1:
                criteria = new_number(criteria, "0000", 'west')

            # if neighbors are initialized, check there criteria to generate the criteria :
            if row != 0 and rooms[row-1][col].initialized:
                criteria = new_number(criteria, rooms[row-1][col].number, 'south')
            if row != size-1 and rooms[row+1][col].initialized:
                criteria = new_number(criteria, rooms[row+1][col].number, 'north')
            if col != 0 and rooms[row][col-1].initialized:
                criteria = new_number(criteria, rooms[row][col-1].number, 'east')
            if col != size-1 and rooms[row][col+1].initialized:
                criteria = new_number(criteria, rooms[row][col+1].number, 'west')

            # modify room :
            rooms[row][col].rect.x += ((-size//2)+col+1)*rooms[row][col].rect.w
            rooms[row][col].rect.y += ((-size//2)+row+1)*rooms[row][col].rect.h
            for i in range(4):
                if criteria[i] == '1' or criteria[i] == '0':
                    tmp = list(rooms[row][col].number)
                    tmp[i] = criteria[i]
                    rooms[row][col].number = "".join(tmp)
                else:
                    tmp = list(rooms[row][col].number)
                    tmp[i] = randint(0, 1)
                    rooms[row][col].number = "".join(tmp)
            rooms[row][col].walls = get_walls(rooms[row][col].number, rooms[row][col].rect)
            rooms[row][col].image = pygame.image.load("./images/rooms/room_" + rooms[row][col].number + ".png")
            # rooms[row][col].special = special
            rooms[row][col].initialized = True
            rooms[row][col].position = (((-size//2)+col+1), ((-size//2)+row+1))

    return rooms


def new_number(new, number, direction_to_generate):
    if direction_to_generate == 'south':
        tmp = list(new)
        tmp[3] = number[1]
        new = "".join(tmp)
    elif direction_to_generate == 'north':
        tmp = list(new)
        tmp[1] = number[3]
        new = "".join(tmp)
    elif direction_to_generate == 'east':
        tmp = list(new)
        tmp[0] = number[2]
        new = "".join(tmp)
    elif direction_to_generate == 'west':
        tmp = list(new)
        tmp[2] = number[0]
        new = "".join(tmp)
    return new
