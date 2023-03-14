
Final Project
=======================

# Hypothesis and Background:

Over the quarter while working on ludobots and other assignments, I became curious as to what might happen if I started to tinker with the gravity during simulations, especially if I changed it during different parts of evolution. Given the liberty to explore what I wanted to for my final project, I decided to do just that.

## The experiment

I set out to evolve creatures in 3 locations: Earth, Luna, and Jupiter.

Earth has a gravitational constant of -9.8m/s^2, and since, as residents of Earth, we're all familiar with how that feels and also since that's been the gravity setting for all of our other assignments, I'm treating this as the control group.

Luna has a gravitational constant of -1.6 m/s. I chose this because it's significantly different than Earth's and because we're also familiar with, or at least, have some imagination of, what gravity might feel like there.

Jupiter has a gravitational constant of -24.8m/s. I chose this because it's the strongest gravity in our solar system, and because Luna strayed the opposite extreme relative to earth.



### Setup

I trained creatures on each of these planets. I used 5 different seeds (for parallel hill climbers), and evolved each with a population size of 100 for 250 generations each. See their fitnesses below (or watch the video to see them in action):



[Insert graph]


(Parallel hill climbers evolve a population but creatures with different parents aren't compared to each other during selection: only creatures from the same parents).


### The test

Once all these creatures were trained, I put them back in each environment and trained them (briefly) once more. More specifically, I took each of the 5 best robots trained on each planet, and trained them some more on each planet. This time, I used a population size of 10 and trained each for 25 generations. I chose a smaller simulation because I knew I'd have to do this many times (because it was a lot of tinkering), and didn't have (3 hours x however many times I needed to run it) to spare.

My fitness function was how far they traveled in terms of x-distance.


### Hypothesis

I think that the creatures trained on each planet will perform the best when retrained and evaluated on their own planets. However, the performance of the robots trained on the other planets will be harder to predict. I would guess that the creatures initially trained under high gravity (Jupiter) will perform better than those that were trained under low gravity (Luna) since that's what I would expect of humans. A person who has lived their life under high stress is stronger and better suited for most environments than someone who never had to exert much energy to get around since gravity was so low.

I also predict that the creatures initially trained on Luna will tend to "jump" to get around, while creatures on Jupiter will be forced to crawl under the gravitational pull of their planet forcing them toward the ground.


### Results


#### Here's how the robots did on average in the control environment:

![Averages on Earth](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/averages_control.png?raw=true)

Each line represents the average fitness creatures initially trained on the specified planet when all were retrained and evaluated on Earth (the control planet). As you can see, the creatures initially trained on Earth did the best on Earth.

All three groups of creatures increased their fitness over the course of their evolution on Earth, but the most staggering improvement was that of the creatures initially trained on the moon, who increased their average fitness by over eight points.


Let's take a closer look at those Moon creatures:

![Luna creatures on earth](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/MoonInControl.png?raw=true)

We see a pretty wide range of starting fitnesses, and all of them improved similarly. However, when we look at how the individual Jupiter creatures did on earth, we don't find the same thing:

![Jupiter creatures on earth](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/JupiterInControl.png?raw=true)

Here, two of the creatures improved quite a bit, but two of them barely improved, and one didn't improve at all!





#### Here's how the creatures did, on average, on Luna:

![Averages on Luna](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/averages_moon.png?raw=true)

Here, the performance of creatures initially trained on Luna did far better than the rest. However, the increase in fitness of the other two groups was more significant. While the average fitness of creatures initially trained on Luna increased about one to two points, the other two groups average a five to seven point increase!

Let's first look at the Luna creatures individually:
![Luna on luna](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/MoonInMoon.png?raw=true)

There's not much improvement here at all. I suppose this makes sense, given that they had a lot of time to improve when they evolved initially, but very little time (relatively) when they were placed again on Luna. The environment hadn't changed, so why should they?

How about the creatures from Jupiter?
![Jupiter on luna](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/JupiterInMoon.png?raw=true)

Here, the average increase was about three and half to four points. The Jupiter bots experienced the most "shock", in that their environments had changed the most. It makes sense that this would cause them to change more (relative to the Luna creatures).


#### Here's how creatures did, on average, on Jupiter:

![Averages on Jupiter](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/averages_jupiter.png?raw=true)

This graph is the most jarring. Relative to the Jupiter creatures, the other two groups changed *severly*. 

Here are the Jupiter creatures individually:

![Jupiter on jupiter](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/JupiterInJupiter.png?raw=true)

Very little change. Again, their environment didn't change, so why should they? Luna and Earth creatures, on the other hand:

![luna on jupiter](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/MoonInJupiter.png?raw=true)

![earth on jupiter](https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/ControlInJupiter.png?raw=true)

Wow! These robots improved drastically. The high gravity posed a significant environmental change that the Luna and Earth robots were well suited to adapt to, and they increased their fitness by about ten points each.

## Conclusions

My hypothesis that creatures trained on each planet would perform the best when placed on the same planet held true for both Luna and Earth. However, it failed for Jupiter. When the three groups were placed on Jupiter to further evolve, the robots from Jupiter began with the highest fitness, but soon were surpassed by both the group of robots from Earth and those from Luna.

What does this mean? Training robots in high gravity environments leads to poor performance in other environments? Training robots in low gravity environments makes them more adaptable in higher ones?

I don't know. Further work would include more thourough evolution in new environments (increasing the number of geenrations and population size), as well as trying out different gravitational constants. I only tried three. Perhaps training them on a more continous scale (or, at least, a discrete scale more closely resembling a continous one) would yield more interesting and conclusive results.

# Details


## How I generate creatures
First we roll a 10 sided die to choose how many links our creature will have. We generate the torso, and then to creatre
the rest of the body of the creature, we roll a 3 sided die to choose which direction the next link will face (stemming from the previously added link).

Initially, every joint has a motor in my creatures, and I add a sensor with 1/2 probability.

## How creatures mutate each generation
Every child mutates with the following probabilities:

    * Remove motor Neuron / Add motor neuron (each with 1/20 probability) 
    * Change neuron weight (3/4)
    * Add / Remove sensor neuron (1/5)
    * Add link (1/20)
    * Remove link (1/20)

## Diagrams

Creature Generation (body on top, brain on bottom):


<img src="https://github.com/joshualevitas/final_project_artificiallife/blob/main/Graphs/IMG_0125.jpg?raw=true"  width="600" height="300">



Creature Generation Diagram
==========================



   
Creature Mutation Diagram
=========================
![Creature Mutation](https://github.com/austin-py/ArtificialLife/blob/1287086658b21dccd191fafcf91148e8217c4194/creature_mutation.jpg)


Selection:
==========
Selection algorithm was varried, as detailed in the experimental results below. However the fitness measure remained the same. Namely how far the creature could travel from the origin in any direction. 

Experimentation:
=======================
For the purpose of experimentation, 420,000 simulations were run. The full writeup of the results and more details can be found [Here](https://github.com/austin-py/ArtificialLife/blob/final-project/Final_Writeup.md)


TO RUN: 
===================
Simply run "python3 main.py" and it will simulate 5 hill climbers which each have 10 members of population for 10 generations. Only the best from each hill climber run is shown visually, and only when show=True in main.py. The fitness values of the creatures will be saved in the whatever file the variable "FILE NAME" points to within the Data folder.

You are also able to comment out lines 9-14, and uncomment lines 16-18 to simulate one robot that was the result of evolution.

Viewing can be slowed down by adjusting the sleep time in constants. 


Documentation:
==============
To view a 10 teaser gif: https://youtu.be/STcML44qikA  <br>
To view a summary video of the work:  https://youtu.be/rgEhXUmA4ew <br>
Bloopers: https://youtu.be/1omTaGXlKPc <br>
To view one creature in both an evolved and random state: https://youtu.be/_wVzwvb8V4w <br>
To view an evolutionary run of one creature (every 50 generations is shown): https://youtu.be/Oq9HjgO-8LM <br>



Citations:
===========

Credit to /r/ludobots and pyrosim. All of my work is on top of these two sources, and relies heavily on the work of these two sources in order to try to learn something new. 

Also to Karl Sims and Sam Kriegman and his Artifical Life Class.








