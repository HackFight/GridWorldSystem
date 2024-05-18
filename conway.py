import os, math, pygame, grid_system, algorithms, renderer, recorder

GRID_HEIGHT, GRID_WIDTH = (100, 100)
MIN_SPEED = 1
PIXEL_SIZE = 6

white = (252, 251, 244)
black = (20, 25, 24)
purple = (186, 85, 255)

# Pygame init
pygame.init()

# Screen init
SCREEN_WIDTH = PIXEL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = PIXEL_SIZE * GRID_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
font = pygame.font.SysFont("Classic Console Neue", 16)

#UI texts init
UI_texts = []
UI_texts.append(font.render("Space bar - pause", True, purple))
UI_texts.append(font.render("Mousewheel - speed", True, purple))
UI_texts.append(font.render("LMB - draw", True, purple))
UI_texts.append(font.render("S - screenshot", True, purple))
UI_texts.append(font.render("C - clear", True, purple))
UI_texts.append(font.render("U - change UI", True, purple))
UI_texts.append(font.render("R - start/stop recording", True, purple))

def WriteGrid(grid):

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            print(grid[x][y], end = "  ")
        
        print("")

def UpdateScreen(_grid, dynamic_UI, Show_UI = True):

    # Clear screen
    renderer.ClearScreen(screen)

    # Render grid
    renderer.DrawGrid(_grid, GRID_WIDTH, GRID_HEIGHT, screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Render UI
    if Show_UI:
        #Left
        i= 0
        for text in UI_texts:
            screen.blit(text, (10, 10 + text.get_height() * i))
            i += 1

        #Right
        j = 0
        for text in dynamic_UI:
            screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10 + text.get_height() * j))
            j += 1
    else:
        pass

    # Update screen
    pygame.display.flip()

def main():
    # Variables init
    ticking = True
    clicked = False
    recording = False
    scroll = 0
    steps = 0
    UI_mode = 1
    simulation_time = 0
    last_step_time = 0
    frame = 0
    recording_date = ""

    # Grid init
    grid = grid_system.GridInit(GRID_WIDTH,GRID_HEIGHT)

    # Cells init
    grid[1][0] = 1
    grid[2][1] = 1
    grid[2][2] = 1
    grid[1][2] = 1
    grid[0][2] = 1

    # Clock init
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:

        clock.tick()

        if recording:
            recorder.CaptureVideoFrame(screen, frame, "Recording_" + recording_date)
            frame += 1

        # Inputs ########################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                # Pause if spacebar pressed
                if event.key == pygame.K_SPACE:
                    ticking = not ticking

                # Screenshot if S key pressed
                if event.key == pygame.K_s:
                    recorder.Screenshot(screen, "Conways-" + str(GRID_WIDTH) + "x" + str(GRID_HEIGHT))
                
                # Clear simulation if C key pressed
                if event.key == pygame.K_c:
                    grid = grid_system.GridInit(GRID_WIDTH, GRID_HEIGHT)
                    steps = 0
                    simulation_time = 0
                    last_step_time = 0

                    if not UI_mode == 0: UpdateScreen(grid, dynamic_texts, True)
                    else: UpdateScreen(grid, dynamic_texts, False)

                # Change UI mode if U key pressed
                if event.key == pygame.K_u:
                    UI_mode += 1
                    if UI_mode > 2: UI_mode = 0

                # Toggle recording with R
                if event.key == pygame.K_r:
                    if not recording:
                        recording = True
                        recording_date = recorder.GetDate()
                        dir = "Recording_" + recording_date
                        os.mkdir(dir)
                    else:
                        recording = False
                        recorder.MakeMP4(dir, dir, 60)
                        try:
                            files = os.listdir(dir)
                            for file in files:
                                file_path = os.path.join(dir, file)
                                if os.path.isfile(file_path):
                                    os.remove(file_path)
                            os.rmdir(dir)
                            print("All files deleted successfully.")
                        except OSError:
                            print("Error occurred while deleting files.")

            # Change simulation speed with mousewheel
            if event.type == pygame.MOUSEWHEEL:
                scroll += int(event.y)
                if scroll < 0: scroll = 0
                elif scroll > 10: scroll = 10

            # Draw if LMB pressed
            if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
                selected_pixel_x = math.floor(pygame.mouse.get_pos()[0] / PIXEL_SIZE)
                selected_pixel_y = math.floor(pygame.mouse.get_pos()[1] / PIXEL_SIZE)
                ticking = False

                if not clicked:
                    state = grid_system.Switch(grid, selected_pixel_x, selected_pixel_y)
                if selected_pixel_x > 0 and selected_pixel_x < GRID_WIDTH and selected_pixel_y > 0 and selected_pixel_y < GRID_HEIGHT:
                    # Switch pixel state
                    grid[selected_pixel_x][selected_pixel_y] = state

                    # Add pixel on screen
                    if UI_mode == 0: UpdateScreen(grid, dynamic_texts, False)
                    else: UpdateScreen(grid, dynamic_texts, True)
                clicked = True
            else:
                clicked = False

        #########################################################3
        # Dynamic variables
        simulation_speed = MIN_SPEED - (scroll / 10)

        # Dynamic texts
        dynamic_texts = []

        if UI_mode == 0:
            UpdateScreen(grid, dynamic_texts, False)
            pass
        else:
            # Speed stat
            try:
                steps_per_second = 1/simulation_speed
                actual_speed_text = font.render("Speed: " + str(int(steps_per_second)) + " steps/second", True, purple)
            except:
                actual_speed_text = font.render("Speed: MAX", True, purple)
            dynamic_texts.append(actual_speed_text)

            if UI_mode == 2:
                # Steps
                steps_text = font.render("Steps: " + str(steps), True, purple)
                dynamic_texts.append(steps_text)

                # Simulation time
                time_text = font.render("Simulation time: " + str(simulation_time/1000), True, purple)
                dynamic_texts.append(time_text)

            # Recording
            if recording:
                recording_text = font.render("Recording", True, purple)
                dynamic_texts.append(recording_text)

            # Paused
            if not ticking:
                paused_text = font.render("Simulation paused", True, purple)
                dynamic_texts.append(paused_text)
            
            UpdateScreen(grid, dynamic_texts, True)

        
        # Simulation ######################################################
        if ticking:
            simulation_time += clock.get_time()

            now = simulation_time / 1000
            if now - last_step_time >= simulation_speed:
                steps += 1
                last_step_time = now

                # Next gen
                grid = algorithms.Conway(grid, GRID_WIDTH, GRID_HEIGHT)

                # Update screen
                if not UI_mode == 0: UpdateScreen(grid, dynamic_texts, True)
                else: UpdateScreen(grid, dynamic_texts, False)

    pygame.quit()

if __name__ == '__main__':
    main()