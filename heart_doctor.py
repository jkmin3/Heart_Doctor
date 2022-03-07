import pygame

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Doctor")

walkDown = [pygame.image.load('games/01.png'), pygame.image.load('games/02.png'), pygame.image.load('games/03.png')]
walkLeft = [pygame.image.load('games/04.png'), pygame.image.load('games/05.png'), pygame.image.load('games/06.png')]
walkRight = [pygame.image.load('games/07.png'), pygame.image.load('games/08.png'), pygame.image.load('games/09.png')]
walkUp = [pygame.image.load('games/10.png'), pygame.image.load('games/11.png'), pygame.image.load('games/12.png')]
MaxHR = pygame.image.load('MaxHR_for_Sex.png')
CPT = pygame.image.load('CPT.png')
Two_Chart = pygame.image.load('Two_Charts.png')
Scatter = pygame.image.load('Scatter.png')
hospital = pygame.image.load('hospital.png')


BLUE = (22, 184, 233)
PURPLE = (178, 121, 236)
RED = (236, 108, 108)
GREEN = (67, 233, 176)
ORANGE = (250, 159, 54)
main_room = (200, 170, 100)


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.VEL = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

    def draw(self, win):  # This function allows the sprite to be animated
        if self.walkCount + 1 >= 60:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount // 20], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 20], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(walkDown[self.walkCount // 20], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            win.blit(walkUp[self.walkCount // 20], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(walkDown[1], (self.x, self.y))

    @staticmethod
    def doc_movement(keys, doc, border):  # This is for the doctor's movements and so that it can't go through the border
        if keys[pygame.K_LEFT]:
            doc.x -= doc.VEL
            doc.left = True
            doc.right = False
            doc.up = False
            doc.down = False
            if doc.x < 0 + border[0].width - 5 and doc.y < border[0].height:  # 1st border
                doc.x += doc.VEL
                doc.left = False
            if doc.x < 0 + border[1].width - 5 and doc.y > border[1].y - doc.height:  # 2nd border
                doc.x += doc.VEL
                doc.left = False
        elif keys[pygame.K_RIGHT]:
            doc.x += doc.VEL
            doc.left = False
            doc.right = True
            doc.up = False
            doc.down = False
            if doc.x > WIDTH - border[2].width - doc.width + 5 and doc.y < border[2].height:  # 3rd border
                doc.x -= doc.VEL
                doc.right = False
            if doc.x > WIDTH - border[3].width - doc.width + 5 and doc.y > border[3].height + doc.height:  # 4th border
                doc.x -= doc.VEL
                doc.right = False
        elif keys[pygame.K_UP]:
            doc.y -= doc.VEL
            doc.left = False
            doc.right = False
            doc.up = True
            doc.down = False
            if doc.y < border[4].height and doc.x < border[4].width + 5:  # 5th border
                doc.y += doc.VEL
                doc.up = False
            if doc.y < border[5].height and doc.x > border[5].x - doc.width:
                doc.y += doc.VEL
                doc.up = False
        elif keys[pygame.K_DOWN]:
            doc.y += doc.VEL
            doc.left = False
            doc.right = False
            doc.up = False
            doc.down = True
            if doc.y > HEIGHT - border[6].height - doc.height and doc.x < border[6].width + 5:  # 6th border
                doc.y -= doc.VEL
                doc.down = False
            if doc.y > HEIGHT - border[7].height - doc.height and doc.x > border[7].x - doc.width:  # 6th border
                doc.y -= doc.VEL
                doc.down = False
        else:
            doc.left = False
            doc.right = False
            doc.up = False
            doc.down = False
            doc.walkCount = 0


class Wall(object):  # This class will be building all the rooms with "walls"
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Room(object):
    def __init__(self):
        self.wall_list = []

    def draw(self, win):
        for w in self.wall_list:
            wall = w.rect()
            pygame.draw.rect(win, w.color, wall)


class Room1(Room):
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 330, 20, PURPLE],
                 [450, 0, 330, 20, PURPLE],
                 [20, 580, 330, 20, PURPLE],
                 [450, 580, 330, 20, PURPLE]]

        for item in walls:
            w = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.append(w)


class Room2(Room):
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 350, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [20, 580, 760, 20, RED]]

        for item in walls:
            w = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.append(w)


class Room3(Room):
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 350, GREEN],
                 [0, 350, 20, 250, GREEN],
                 [780, 0, 20, 250, GREEN],
                 [780, 350, 20, 250, GREEN],
                 [20, 0, 760, 20, GREEN],
                 [20, 0, 760, 20, GREEN],
                 [20, 580, 760, 20, GREEN],
                 [20, 580, 760, 20, GREEN]]

        for item in walls:
            w = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.append(w)


class Room4(Room):
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 350, ORANGE],
                 [0, 350, 20, 250, ORANGE],
                 [780, 0, 20, 350, ORANGE],
                 [780, 350, 20, 250, ORANGE],
                 [20, 0, 760, 20, ORANGE],
                 [20, 0, 760, 20, ORANGE],
                 [20, 580, 330, 20, ORANGE],
                 [450, 580, 330, 20, ORANGE]]

        for item in walls:
            w = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.append(w)


class Room5(Room):
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 350, BLUE],
                 [0, 350, 20, 250, BLUE],
                 [780, 0, 20, 350, BLUE],
                 [780, 350, 20, 250, BLUE],
                 [20, 0, 330, 20, BLUE],
                 [450, 0, 330, 20, BLUE],
                 [20, 580, 760, 20, BLUE],
                 [20, 580, 760, 20, BLUE]]

        for item in walls:
            w = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.append(w)


FPS = 60
doctor = Player(300, 400, 48, 48)


def main():  # This is the main function which keeps the game running
    clock = pygame.time.Clock()
    run = True
    rooms = []
    r1 = Room1()
    r2 = Room2()
    r3 = Room3()
    r4 = Room4()
    r5 = Room5()

    rooms.append(r1)
    rooms.append(r2)
    rooms.append(r3)
    rooms.append(r4)
    rooms.append(r5)

    current_room_no = 0
    current_room = rooms[current_room_no]
    color = main_room
    background = hospital
    coordinates = (155, 130)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if doctor.x < -10:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                doctor.x = 790
                color = BLUE
                background = Scatter
                coordinates = (80, 60)
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                doctor.x = 790
                color = main_room
                background = hospital
                coordinates = (155, 130)

        if doctor.x > 800:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                doctor.x = 0
                color = GREEN
                background = Two_Chart
                coordinates = (80, 60)
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                doctor.x = 0
                color = main_room
                background = hospital
                coordinates = (155, 130)

        if doctor.y < -10:
            if current_room_no == 0:
                current_room_no = 3
                current_room = rooms[current_room_no]
                doctor.y = 590
                color = PURPLE
                background = MaxHR
                coordinates = (80, 60)
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                doctor.y = 590
                color = main_room
                background = hospital
                coordinates = (155, 130)

        if doctor.y > 600:
            if current_room_no == 0:
                current_room_no = 4
                current_room = rooms[current_room_no]
                doctor.y = 0
                color = ORANGE
                background = CPT
                coordinates = (80, 60)
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                doctor.y = 0
                color = main_room
                background = hospital
                coordinates = (155, 130)

        keys = pygame.key.get_pressed()
        doctor.doc_movement(keys, doctor, current_room.wall_list)
        WIN.fill(color)
        WIN.blit(background, coordinates)
        doctor.draw(WIN)
        current_room.draw(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
