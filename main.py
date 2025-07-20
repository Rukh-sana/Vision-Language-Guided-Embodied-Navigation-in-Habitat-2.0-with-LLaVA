import subprocess
import requests
import base64
import time
import os
import cv2


def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def query_llava(prompt, image_paths):
    images_b64 = [encode_image(path) for path in image_paths]
    payload = {
        "model": "llava",
        "prompt": prompt,
        "images": images_b64,
        "stream": False
    }
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    response.raise_for_status()
    return response.json()["response"].strip().lower()


def press_key(action):
    key_map = {
        "forward": "w",
        "backward": "s",
        "left": "a",
        "right": "d",
    }
    key = key_map.get(action)
    if key:
        try:
            for _ in range(10):
                subprocess.run(["xdotool", "key", key], check=True)
                time.sleep(0.1)
        except subprocess.CalledProcessError:
            print(f"Failed to send key '{key}' using xdotool.")
    else:
        print(f"Unknown action from LLaVA: '{action}'")


def focus_habitat_window():
    try:
        subprocess.run(["xdotool", "search", "--name", "Habitat", "windowactivate"], check=True)
        time.sleep(0.5)
    except subprocess.CalledProcessError:
        print("Failed to focus Habitat window. Is it running and titled correctly?")


def capture_screenshot(output_path):
    try:
        subprocess.run(["import", "-window", "Habitat Sim Interactive Viewer", output_path], check=True)
    except subprocess.CalledProcessError:
        print("Failed to capture screenshot. Is the window titled 'Habitat Sim Interactive Viewer'?")


def launch_habitat_viewer():
    launch_script = """
#    source ~/miniconda3/etc/profile.d/conda.sh
    source ~/anaconda3/etc/profile.d/conda.sh
    conda activate habitat
    cd ~/habitat-sim
    python examples/viewer.py --dataset data/replica_cad/replicaCAD.scene_dataset_config.json --scene apt_2
    """
    return subprocess.Popen(["bash", "-c", launch_script])


def close_previous_start_img():
    try:
        output = subprocess.check_output(["wmctrl", "-l"]).decode()
        for line in output.splitlines():
            if "start_img" in line:
                win_id = line.split()[0]
                subprocess.run(["wmctrl", "-i", "-c", win_id], check=True)
                print("🧹 Closed previous 'start' window.")
                return
    except subprocess.CalledProcessError:
        print("⚠️ No previous 'start' window found or could not close it.")


if __name__ == "__main__":
    current_image_path = "/home/rukh/Pictures/Screenshots/replicaStartImg.png"
    goal_image_path = "/home/rukh/Pictures/Screenshots/goalImg.png"

    prompt = """
You are a navigation agent inside an indoor environment.

You can move using only these four actions: forward, backward, left or right.

The first image is your current view. The second image is your goal view.

Analyze both images and decide what action should be taken to get closer to the goal.

Reply with only one word: forward, backward, left or right.
"""

    # Show initial images
    img_current = cv2.imread(current_image_path)
    img_goal = cv2.imread(goal_image_path)

    cv2.namedWindow("start_img", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("goal_img", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("start_img", img_current)
    cv2.imshow("goal_img", img_goal)

    print("📸 Press any key in an image window to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Launch Habitat simulator
    sim_process = launch_habitat_viewer()
    print("Waiting for Habitat simulator to launch...")
    time.sleep(10)

    print("LLaVA Model loading...\n")

    try:
        for i in range(1, 31):
            if i == 1:
                print("✅ LLaVA model loaded.")
                print(f"\nPrompt:\n{prompt}\n")

            print(f"\n🔁 Step {i}")
            focus_habitat_window()
            capture_screenshot(current_image_path)

            # Read and show the updated current image
            img_current = cv2.imread(current_image_path)
            cv2.namedWindow("start_img", cv2.WINDOW_AUTOSIZE)
            cv2.imshow("start_img", img_current)
            cv2.waitKey(1)

            # Ask LLaVA for the next action
            action = query_llava(prompt, [current_image_path, goal_image_path])
            print(f"🚶 Action {i}: {action}")

            if "goal" in action or "found" in action:
                print("🎯 Goal found. Exiting loop.")
                break

            press_key(action)
            time.sleep(2)

        cv2.destroyAllWindows()

    except Exception as e:
        print("❌ Error during navigation loop:", e)
        cv2.destroyAllWindows()
    finally:
        sim_process.terminate()
        print("🛑 Goal Not Found.")
        print("🛑 Simulator terminated.")
