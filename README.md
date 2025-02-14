# 🕌 Azan Mute Windows App

## 🎯 Overview
Azan Mute is a **Windows application** that automatically **mutes system audio** when the **Azan (Call to Prayer)** is detected and unmutes it afterward. It uses **OpenAI Whisper** for speech-to-text recognition and **FFmpeg** for audio processing.

## 🛠 Features
✅ **Listens to system audio (not microphone)**  
✅ **Detects Azan phrases from any source (YouTube, MP3, Mosque speakers, etc.)**  
✅ **Works offline using OpenAI Whisper**  
✅ **Mutes Windows sound during Azan and unmutes after 2 minutes**  
✅ **Runs in the background and can exit by pressing `Q`**  

---

## 📦 Installation

### **1️⃣ Install Dependencies**
Run the following command to install required Python packages:
```sh
pip install openai-whisper ffmpeg numpy torch sounddevice keyboard
