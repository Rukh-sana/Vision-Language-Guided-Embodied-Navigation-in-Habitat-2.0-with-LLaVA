# Vision-Language-Guided-Embodied-Navigation-in-Habitat-2.0-with-LLaVA
This project uses Habitat 2.0 and LLaVA to enable an agent to navigate 3D scenes by comparing images and following vision-language-based commands. 
Vision-Language Navigation Agent in Habitat 2.0
This project demonstrates an autonomous navigation agent inside a photorealistic 3D environment using Facebook AI's Habitat-Sim and the ReplicaCAD Baked Lighting dataset. It integrates the LLaVA vision-language model to interpret visual goals and generate movement commands within the simulated space.

By comparing the agent’s current view with a target view, the system uses LLaVA to generate commands like forward, left, right, or backward. These are executed in real time using Habitat’s viewer, enabling vision-guided embodied navigation.

Key Components
Habitat-Sim (https://github.com/facebookresearch/habitat-sim)

ReplicaCAD Baked Lighting dataset

LLaVA (Large Language and Vision Assistant)

OpenCV for visual feedback

xdotool and import for keyboard and screen automation

What It Does
Launches a Habitat interactive simulation

Captures and displays the agent’s current and goal views

Uses LLaVA to infer movement direction from image comparison

Executes movement commands in real time using system-level automation.

Requirements
Linux environment with GUI

Python 3.8+

LLaVA API running locally

Habitat-Sim installed and configured

Acknowledgments
This project builds on the outstanding open-source work from Facebook AI Research (FAIR) and the LLaVA team.
