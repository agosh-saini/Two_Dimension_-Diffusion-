# Two_Dimension_Diffusion
Diffusion explained from Random Walk point of view and a simulation of Fick's law in 2D space

# What is Diffusion
Diffusion is a process where a fluid of high concentration can disperese in another fluid completely. 
This process is why we can mix things gasses together and liquids together. This is also why if you spray febreze in one corner of a room, it then spreads everywhere in the room


# Random Walk
You can [click here](https://en.wikipedia.org/wiki/Random_walk) to read more about Random walk. Lets take a single molecule in a 2D space. We will only look at it from  an X point of view, completely ingoring the other dimension. 
If you take this molecule, what are the chances it will move in the left or right direction? 
First answer that comes to mind is 1/3 but the actual answer is 1/5. That is because it can also move in either Y direction without moving in X plane and it can also choose not to move. 
This random motion is caused by the inherent random energy a molecule can have. 
This same process occurs in Y plane as well. 
If we look at how it functions together, we end up with the following graphs

![alt text](https://github.com/agosh-saini/Two_Dimension_Diffusion/blob/master/Random_walk/10000_molecules_after_1_movements.png?raw=true)
![alt text](https://github.com/agosh-saini/Two_Dimension_Diffusion/blob/master/Random_walk/10000_molecules_after_10_movements.png?raw=true)
![alt text](https://github.com/agosh-saini/Two_Dimension_Diffusion/blob/master/Random_walk/10000_molecules_after_100_movements.png?raw=true)
![alt text](https://github.com/agosh-saini/Two_Dimension_Diffusion/blob/master/Random_walk/10000_molecules_after_1000_movements.png?raw=true)

# Diffusion In 2D Space
[Fick's laws of diffusion](https://www.google.com) explain how diffusion will occur in any space. An Implimentation of his equations can be foudn in [Fick's Law folder](https://github.com/agosh-saini/Two_Dimension_-Diffusion-/tree/master/Ficks_law_Diffusion). 
If you want to run the files for your self:
Step 1: Run the [ficks_2d_diffusion.py](https://github.com/agosh-saini/Two_Dimension_Diffusion/blob/master/Ficks_law_Diffusion/ficks_2d_diffusion.py) 
Step 2: Run [create_video.py](https://github.com/agosh-saini/Two_Dimension_Diffusion/blob/master/Ficks_law_Diffusion/create_video.py)

Note - For the file in step 2, I cannot find the sources I used for the file as I made the file a while ago and lost the file where I recorded my sources. 

# What Diffusion Looks Like
Here is an example of how diffusion may look in a 2D space

[![Diffusion In A 2D Space](https://img.youtube.com/vi/Ww4VwPqWFYc/0.jpg)](https://www.youtube.com/watch?v=Ww4VwPqWFYc "Diffusion In A 2D Space")
