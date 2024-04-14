
# BeagleDOOM

Welcome to the BeagleDOOM project repository! This project is an attempt to run an open-source clone of the classic 1993 DOOM game on a Beaglebone board with a custom-built controller. This README provides an overview of the project, installation instructions, and usage details.

## Project Overview

**System Purpose:** The purpose of BeagleDOOM is to recreate the classic gaming experience of DOOM with a twist—using a custom controller. This controller integrates an 8x8 LED Matrix and a two-row LCD to display real-time player statistics such as Health level, Armor level, and Kill count.

**System Implementation:**
- **Hardware:** The project uses a Beaglebone board to run the game and a Raspberry Pi Pico to handle the custom controller inputs and display outputs. The controller includes a joystick, an LED matrix, an LCD display, a potentiometer, digital input buttons, and a 3D-printed shell casing.
- **Software:** The game engine is a modified version of Chocolate DOOM which has been customized to integrate with the hardware controller for an immersive experience. Player data is managed by the Raspberry Pi Pico and displayed on the controller in real-time.

### Key Components
- Beaglebone Black with HDMI output
- Raspberry Pi Pico
- Custom 3D-printed controller housing
- Joystick, 8x8 LED matrix, 2-row LCD display
- Potentiometer and digital input buttons for game interaction
- Small 720P TV Screen for display

### Software and Libraries
- Modified Chocolate DOOM source code
- CircuitPython with Adafruit libraries for hardware interfacing

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-repo/BeagleDOOM.git
   cd BeagleDOOM
   ```

2. **Setup the Hardware:**
   - Assemble the hardware according to the circuit diagrams provided in the `docs` folder.
   - Connect the Beaglebone and Raspberry Pi Pico as per the system architecture.

3. **Install Dependencies:**
   - Install the required CircuitPython libraries on the Raspberry Pi Pico.
   - Ensure that the Beaglebone is configured to run the modified DOOM game.

4. **Load the Software:**
   - Flash the Raspberry Pi Pico with the provided firmware.
   - Load the Chocolate DOOM game onto the Beaglebone.

## Usage

To start the game:
1. Power up the Beaglebone and the Raspberry Pi Pico.
2. Use the joystick to navigate the game menus.
3. Play DOOM using the custom controller, and observe your game stats in real-time on the LCD and LED displays.

## Acknowledgements

- Chocolate DOOM community for the base game engine.
- Freedoom project for additional game levels.
- All project contributors and the open-source community.

## Demo

https://github.com/ManrajSRai/beagle-DOOM/assets/74273268/a41fec15-fce6-4803-a391-b60bb30550ae

![setup](https://github.com/ManrajSRai/beagle-DOOM/assets/74273268/f284ec7b-15e2-4a73-aec9-ae5344781172)



For detailed documentation on the hardware setup and the full list of software dependencies, please refer to the pdf files
