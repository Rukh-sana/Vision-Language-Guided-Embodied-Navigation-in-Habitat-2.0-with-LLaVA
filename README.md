# Vision-Language-Guided-Embodied-Navigation-in-Habitat-2.0-with-LLaVA
This project uses Habitat 2.0 and LLaVA to enable an agent to navigate 3D scenes by comparing images and following vision-language-based commands. 
Vision-Language Navigation Agent in Habitat 2.0


# Vision-Language Navigation with Habitat 2.0 and LLaVA

This project integrates the Habitat 2.0 simulator with the LLaVA vision-language model to enable an agent to navigate 3D indoor environments. The agent compares its current view to a goal image, and LLaVA generates movement commands (forward, left, right, backward) based on visual reasoning.

## 🔧 Features

- Embodied navigation using ReplicaCAD Baked Lighting scenes
- Vision-language reasoning via LLaVA API
- Automated command execution using xdotool and OpenCV
- Real-time screenshot capture and navigation loop

## 🧩 Components

- viewer.py – Modified Habitat interactive viewer
- test_Script.py – Main control loop with LLaVA integration
- LLaVA model/API – Vision-language command generation
- Habitat-Sim – 3D simulation environment

## 💻 Requirements

- Linux OS with GUI
- Python 3.8+
- Habitat-Sim (https://github.com/facebookresearch/habitat-sim)
- LLaVA model/API running locally
- xdotool, wmctrl, import (for automation)

## 🚀 How It Works

1. Launch viewer.py to load a Habitat scene.
2. Capture current and goal images.
3. Send both images to LLaVA for a movement decision.
4. Simulate the keypress using xdotool.
5. Repeat until the goal is reached.

## 📜 License

This project builds on open-source components and is intended for research and educational use.

## 🙏 Acknowledgments

- Facebook AI Research for Habitat-Sim  
- LLaVA team for their vision-language model  
- ReplicaCAD dataset for realistic indoor scenes
