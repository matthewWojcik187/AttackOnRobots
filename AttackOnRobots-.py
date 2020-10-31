# Developers: Adrian Musselwhite, Dennis Dao, Matthew Wojcik , Reid Stewart
# Date: January 29th , 2019
# Attack on Robots - Main Game
# Version 1.0 Beta


"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
 
Explanation video: http://youtu.be/QplXBw_NK5Y
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
 
"""

# Imports
import pygame
from menuLibrary import *
from levelLibrary import *
from playerLibrary import *
 
# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
            
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Pygame init
pygame.init()

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Attack on Robots")

#Game Sound Varibles
jump_sound = pygame.mixer.Sound('jump_sound.ogg')
death_sound = pygame.mixer.Sound('death_sound.ogg')
switch_sound = pygame.mixer.Sound('switch_sound.wav')
door_sound = pygame.mixer.Sound('door_sound.wav')
boom_sound = pygame.mixer.Sound('Explosion.ogg')

# Main proogram loop
def main():
    """ Main Program """
    # Varaibles for the menu.
    onInstructions = 0  
    onmainMenu = 0
    paused = 0
    oncharacterSelect = 0

    # Create the player
    player = Player()
 
    # Create all the levels and appends it to the level list.
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
 
    # Set the current level to a number and assigns it to the level list.
    current_level_no = 0
    current_level = level_list[current_level_no]

    # Sprite list
    active_sprite_list = pygame.sprite.Group()
    # The level the player is on.
    player.level = current_level
    
    # Player's x and y coordinates.
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height -50
    # Adds the player to the active sprite list.
    active_sprite_list.add(player)

    #Sets the background image
    if current_level_no == 0:
        background_image = pygame.image.load("LevelOneBackground.jpg").convert()
    if current_level_no == 1:
        background_image = pygame.image.load("LevelTwoBackground.jpg").convert()
    if current_level_no == 2:
        background_image = pygame.image.load("LevelThreeBackground.png").convert()
    if current_level_no == 3:
        background_image = pygame.image.load("LevelFourBackground.jpg").convert()
        
    # Loop until the user clicks the close button.
    done = False
            
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # In Game Movement for each character.
            # This code only runs after the user has clicked start on the main menu.
            if onmainMenu == 1 and paused == 0 and oncharacterSelect == 0:
                if event.type == pygame.KEYDOWN and player.characterNumber == 1 :
                    # If the left arrow key is pressed the character moves left and the image is changed 
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                        player.image = pygame.image.load("Player 1 Left.png").convert_alpha()
                    # If the right arrow key is pressed the character moves right and the image is changed 
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                        player.image = pygame.image.load("Player 1.png").convert_alpha()
                    # If the up arrow key is pressed the character moves up
                    if event.key == pygame.K_UP: 
                        player.jump()

                # In game movement
                elif event.type == pygame.KEYDOWN and player.characterNumber == 2 :
                    # If the left arrow key is pressed the character moves left and the image is changed 
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                        player.image = pygame.image.load("Player 3 Left.png").convert_alpha()
                    # If the right arrow key is pressed the character moves right and the image is changed 
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                        player.image = pygame.image.load("Player 3.png").convert_alpha()
                    # If the up arrow key is pressed the character moves up
                    if event.key == pygame.K_UP:
                        player.jump()

                # In Game Movement
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()
                if event.type == pygame.KEYDOWN and oncharacterSelect == 0:
                    if event.key == pygame.K_p:
                        switch_sound.play()
                        paused = 1

                        
            # If statements for the menu
            if onmainMenu == 0 and onInstructions == 0:
                menu()
            if onInstructions == 1:
                instructions()
            if paused == 1:
                pauseScreen()
            if oncharacterSelect == 1:
                characterSelect()

            # Mouse position and click
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            # If statement for buttons on main menu
            if click [0] ==1 and onmainMenu == 0 and onInstructions == 0 and oncharacterSelect == 0:
                # Start 
                if 30 < mouse [0] < 185 and 405 < mouse [1] < 482:
                    oncharacterSelect = 1
                    onmainMenu = 1
                    switch_sound.play()                  
                # Instructions
                if 230 < mouse [0] < 600 and 405 < mouse [1] < 482 and onInstructions == 0 and oncharacterSelect == 0:
                    onInstructions = 1
                    switch_sound.play()    
                # Quit
                elif 645 < mouse [0] < 770 and 405 < mouse [1] < 482 and oncharacterSelect == 0 and onInstructions == 0:
                    switch_sound.play()
                    pygame.quit()
                    quit()
                    
            # If statements for button on instructions screen
            if click [0] ==1 and onmainMenu == 0 and onInstructions == 1:
                # Back to main menu button 
                if 270 < mouse [0] < 530 and 500 < mouse [1] < 540:
                    switch_sound.play()
                    main()
                    onInstructions = 0

            # If statements for buttons on pause menu
            if click [0] ==1 and onmainMenu == 1 and paused == 1:
                # Resume button 
                if 285 < mouse [0] < 520 and 180 < mouse [1] < 225:
                    switch_sound.play()
                    paused = 0
                # Main menu button
                if 120 < mouse [0] < 680 and 335 < mouse [1] < 382:
                    switch_sound.play()
                    paused == 0
                    main()
                    
            # If statements for buttons on character select screen        
            # Character 1 runs faster
            # Character 3 jumps higher
            if click [0] ==1 and onmainMenu == 1 and onInstructions == 0 and oncharacterSelect == 1:
                # Character 1 select
                if 85 < mouse [0] < 300 and 160 < mouse [1] < 395:
                    switch_sound.play()
                    player.characterNumber = 1
                    player.image = pygame.image.load("Player 1.png").convert_alpha()
                    oncharacterSelect = 0                    
                # Character 2 select
                if 480 < mouse [0] < 700 and 160 < mouse [1] < 395:
                    switch_sound.play()
                    player.characterNumber = 2
                    player.image = pygame.image.load("Player 3.png").convert_alpha()
                    oncharacterSelect = 0

            # If statements for buttons on pause menu
            if click [0] == 1 and onmainMenu == 1 and paused == 1:                
                # Resume button 
                if 285 < mouse [0] < 520 and 180 < mouse [1] < 225:
                    switch_sound.play()
                    paused = 0  
                # Main menu button
                if 120 < mouse [0] < 680 and 335 < mouse [1] < 382:
                    switch_sound.play()
                    paused == 0
                    main()

            # If statements for buttons on win screen
            if click [0] == 1 and player.won == 1:
                # Back to main button
                if 242 < mouse [0] < 560 and 440 < mouse [1] < 478:
                    switch_sound.play()
                    main()
                                      
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 250:
            diff = 250 - player.rect.left
            player.rect.left = 250
            current_level.shift_world(diff)

        # Gets current position of player.
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            # Sets the current level.
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                # Sets level background and music.
                if current_level_no == 1:
                    background_image = pygame.image.load("LevelTwoBackground.jpg").convert()
                    screen.blit(background_image, [0, 0])
                    pygame.mixer.music.load("second_level_music_new.ogg")
                    pygame.mixer.music.play(-1)
                if current_level_no == 2:
                    background_image = pygame.image.load("LevelThreeBackground.png").convert()
                    screen.blit(background_image, [0, 0])
                    pygame.mixer.music.load("level_3_music_new.ogg")
                    pygame.mixer.music.play(-1)
                if current_level_no == 3:
                    player.onLastLevel = True
                    background_image = pygame.image.load("LevelFourBackground.jpg").convert()
                    screen.blit(background_image, [0, 0])
                    pygame.mixer.music.load("boss_battle.ogg")
                    pygame.mixer.music.play(-1)

        # If the player falls off the screen, they are respawned.
        if player.rect.y > 600:
            if current_level_no != 3:
                player.rect.x = 340 + current_level.world_shift
                player.rect.y = SCREEN_HEIGHT - player.rect.height -50
                death_sound.play()
                player.deathCounter += 1
            else:
                player.rect.x = 340 + current_level.world_shift
                player.rect.y = -10
                death_sound.play()
                player.hitCounter -= 1
                player.deathCounter += 1

        # Sets the first level's music.
        if onmainMenu == 0 and paused == 0 and current_level_no == 0 and oncharacterSelect == 0:
            pygame.mixer.music.load("the_first_level_music.ogg")
            pygame.mixer.music.play(-1)

        # Sets up the death counter text.
        font = pygame.font.SysFont("Calibri", 25, True, False)
        deathText = font.render("Deaths: " + str(player.deathCounter), True, WHITE)
        if current_level_no == 3:
            levelText = font.render("Hits before Timer Reset: " + str(player.hitCounter), True, WHITE)

        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.blit(background_image, [0, 0])
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        screen.blit(deathText, [0, 0])
        if current_level_no == 3 and player.onLastLevel == True:
            deathText = font.render("Deaths: " + str(player.deathCounter), True, WHITE)
            screen.blit(levelText, [0, 25])
            time_output_string = "Time: {0:02}:{1:02}".format(player.minutes, player.seconds)
            clockText = font.render(time_output_string, True, WHITE)
            screen.blit(clockText, [0, 50])
        
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        if onmainMenu == 1 and paused == 0 and oncharacterSelect == 0 and player.won == 0:
            pygame.display.flip()

# Runs the main menu
main()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.

pygame.quit()
