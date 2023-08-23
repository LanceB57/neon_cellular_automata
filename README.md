# Neon Cellular Automata Visualizations

This mini project combines two smaller projects I worked on a few years ago: "neonify"-ing images and playing around with cellular automata.

### 1. Making images neon
A few years ago, a group of friends and I made a web app that had a neon/retro aesthetic, and I found it pretty cool to play around with black-and-white icons and apply a neon glow to them. Got to know how to use PIL through this, and I recently discovered KDTrees which make the process a lot faster. `make_neon.py` is the program that takes a black-and-white image and applies the neon effect to it, ex. `person.png` $\rightarrow$ `neon_person.png`. Just make sure to use the appropriate RGB/RGBA tuples depending on if your image is a jpg/png.
#### `person.png`
![alt text](person.png)
#### `neon_person.png`
![alt text](neon_person.png)


### 2. Cellular automata
This is from a class I took in Chaos & Fractals (and it's also probably the only thing I remember from it lol), where we learned about generating fractal-like structures using cellular automata. For example, B1/S123 generates a pretty cool animation (shown below). 

The code, in `neon_ca.py`, is pretty straightforward, but I definitely see areas that could use some optimization... maybe I'll get to that sometime. It's also a bit janky because I generate each frame as an image then feed those images into an online GIF maker... that could definitely use some work.


Anyways, I thought seeing a cellular automaton model "grow" with a neon effect would look really nice, so enjoy!

#### `result.gif`
![alt text](result.gif)