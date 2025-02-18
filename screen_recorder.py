import cv2
import pyautogui
import numpy as np
import time
import wave
import pyaudio
import threading
from win32api import GetSystemMetrics
from datetime import datetime
import keyboard

# Get screen dimensions
width, height = GetSystemMetrics(0), GetSystemMetrics(1)
dim = (width, height)

# Generate filenames with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
video_filename = f"screen_record_{timestamp}.mp4"
audio_filename = f"audio_{timestamp}.wav"

# Video Writer
output = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'XVID'), 30.0, dim)

# Audio Recording Setup
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
audio_frames = []

# Flags for pause & resume
recording = True
paused = False

# Function to record audio in a separate thread
def record_audio():
    global recording, paused
    while recording:
        if not paused:
            data = stream.read(1024)
            audio_frames.append(data)

# Start the audio recording thread
audio_thread = threading.Thread(target=record_audio)
audio_thread.start()

# Get user-defined duration
duration = int(input("Enter recording duration (in seconds): "))
start_time = time.time()

print("\nControls:")
print(" - Press 'p' to Pause")
print(" - Press 'r' to Resume")
print(" - Press 'q' to Quit")

while time.time() - start_time < duration:
    if keyboard.is_pressed('q'):
        break
    if keyboard.is_pressed('p'):
        paused = True
        print("Recording Paused")
    if keyboard.is_pressed('r'):
        paused = False
        print("Recording Resumed")

    if not paused:
        frame = np.array(pyautogui.screenshot())

        # Draw Mouse Cursor on the Frame
        x, y = pyautogui.position()
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

        # Convert color and write frame
        output.write(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Show FPS Counter
        elapsed_time = time.time() - start_time
        fps = int((elapsed_time + 1) / (time.time() - start_time + 1))
        print(f"\rRecording... FPS: {fps}", end="", flush=True)

recording = False
audio_thread.join()

# Save Audio
stream.stop_stream()
stream.close()
audio.terminate()
wf = wave.open(audio_filename, 'wb')
wf.setnchannels(1)
wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(audio_frames))
wf.close()

output.release()
print(f"\nScreen recording saved as {video_filename}")
print(f"Audio recording saved as {audio_filename}")
