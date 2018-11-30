# Basic optics module
This is a push-fit extension tube that turns a Raspberry Pi camera module into a microscope with a field of view about 400um across and a resolution of around 2um (better than 2um in the case of v2 of the camera module).

This is the optics module for the OpenFlexure Microscope.  It holds a Raspberry Pi camera module and lens, but the lens is reversed and placed 40mm from the sensor, allowing it to function as a high-magnification microscope with a resolution of around 2um.

# Requirements
## Parts
*   1 of [Mechanical holder](./parts/optics_module_plastic_parts)
*   1 of Optics and Sensor
*   1 of [Tools for removing the lens](./parts/camera_lens_removal_tools)


# Assembly Instructions
## Step

First, assemble the necessary tools and parts: the optics module plastic parts (the "objective" and camera board cover), the Raspberry Pi camera module (version 2), the tools for removing the camera lens, two M2 screws to secure the camera.  Depending on print quality, you might also need a sharp craft knife or some tape.

 
NB the lens removal tool, board gripper, and optics module are all specific to the camera you're using.  This version of the instructions is for version 2 of the camera board, if you have v1 it's a similar process but the older versions of the instructions give more detail.  You'll also need to use older STL files, support for v1 of the camera module was removed in v5.17.

 
Later production runs of the Raspberry Pi camera module ship with a lens removal tool included, which is better than the printed tool.  This is a white disc of plastic with a hole in the centre.

 
### Media
*   ![](./images/optics_module_parts.jpg)

## Step
WARNING! The camera board is static sensitive.  Take the usual anti-static precautions (ideally use an anti-static wristband connected to ground, but at the very least make sure you touch an earthed object, such as a metal pipe, before working on the camera module.
### Media
*   ![](./images/static_warning.png)

## Step
We need to remove the lens from the camera.  To do this, you need the two plastic tools (the board gripper and the lens remover) as well as the camera module.  If you are using a USB camera, the lens is held on by two screws from the back, and can be removed by unscrewing these. **Save the screws**, as you will need them later!
### Media
*   ![](./images/picam2_lens_removal_0.jpg)

## Step
Remove the protective film from the camera lens.
### Media
*   ![](./images/picam2_film_removal.jpg)

## Step
There is a small ribbon cable connecting the camera to the PCB that is very easy to break.  There is a square plastic jig that fits over the camera and PCB (the "camera board gripper"), which stops the camera twisting and damaging the ribbon cable.  Fit this over the camera as shown.  Note that the part for v2 of the camera board will sort-of fit v1, but you need to be a little more careful as it's not a perfect fit.
### Media
*   ![](./images/picam2_board_gripper_1.jpg)
*   ![](./images/picam2_board_gripper_2.jpg)

## Step

Next, unscrew the lens from the camera module.  Use the plastic tool to grip the lens module.  This is a small circular part with four prongs that fits over the lens of the camera board (version 2 only) as shown.  To remove the lens, push the removal tool onto the lens (just the top part, with the little plastic flanges) and turn anticlockwise to remove it.

 
The tool only works if the prongs are pointing anticlockwise, so make sure it's the right way round.  You may feel a crack as it starts to move - this is normal.  It's important to use the board gripper to hold the camera chip in place and prevent damage to the delicate ribbon cable.  After you've removed the lens, check that the little black ribbon cable connecting the camera module (the black square of plastic from which you unscrewed the lens) to the PCB is still connected - pop it back in by pushing it with a finger if needed.

 
Once you've removed the lens, be sure to place the camera face down on the desk, or put a piece of tape over the square black lens holder; this will help stop dust settling on the sensor, which is hard to clean.

 
### Media
*   ![](./images/picam2_lens_removal_1.jpg)
*   ![](./images/picam2_lens_removal_2.jpg)
*   ![](./images/picam2_lens_removal_3.jpg)

## Step
Before assembling the parts into the holder, make sure it's free from dust by blowing some air through it, and check there are no strings of plastic in the central hole through the mount.

## Step
Next, put the lens into the holder.  This should just push-fit, but may take a small amount of force, or  require a layer of tape wrapped around the lens to make it fit tightly (depending on your printer).  If it looks like it will require too much force, you might have a different design of camera module and you may need to re-print the part slightly larger (or get a replacement if you bought a kit).  If you wrapped tape around the lens, trim off any tape that protrudes above the lens with a scalpel or sharp craft knife.
### Media
*   ![](./images/lens_insertion_0.jpg)
*   ![](./images/lens_insertion_1.jpg)
*   ![](./images/lens_insertion_2.jpg)
*   ![](./images/lens_insertion_3.jpg)
*   ![](./images/lens_insertion_4.jpg)

## Step
Finally, press the camera module onto the bottom of the optics mount.  It should not be a tight fit, but the cover and two M2 screws will hold it in place in the next step.
### Media
*   ![](./images/optics_assembly_0.jpg)
*   ![](./images/optics_assembly_1.jpg)
*   ![](./images/optics_assembly_2.jpg)

## Step
Place the cover on top of the camera board, then screw the cover and the camera board onto the optics module, using two M2 screws.
### Media
*   ![](./images/camera_screws_1.jpg)



# Notes
This is a push-fit extension tube that turns a Raspberry Pi camera module into a microscope with a field of view about 400um across and a resolution of around 2um (better than 2um in the case of v2 of the camera module).

