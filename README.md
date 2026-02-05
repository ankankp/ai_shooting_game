#  Bullet Hell Shooter Pro + RL Enemy AI

An advanced **Bullet Hell Space Shooter** built using **Python & Pygame**, featuring dynamic enemy waves, boss fights, power-ups, leaderboard system, and an experimental **Reinforcement Learning (DQN) enemy AI**.

---

##  Game Features

*  Multiple Weapons

  * Pistol
  * Double Shot
  * Shotgun
  * Laser
  * Homing Missiles

*  Enemy Types

  * Basic
  * Shooter
  * Homing
  * Kamikaze
  * Sniper
  * Splitter
  * Boss Enemies

*  Wave System

  * Increasing difficulty
  * Boss every 5 waves

*  Power-Ups

  * Rapid Fire
  * Shield
  * Nuke
  * Weapon Upgrade
  * Boss Weapon Drop

*  Health Packs

*  Leaderboard & High Score Saving

* Pause System

* Difficulty Modes

  * Easy
  * Normal
  * Hard

---

##  Reinforcement Learning AI

This project also includes an experimental **Deep Q-Network (DQN) Agent** that can control enemy movement and shooting.

Key components:

* Neural Network model → 
* Experience Replay Buffer → 
* DQN Agent implementation → 
* RL Enemy integration → 
* Training simulation → 

---

## Tech Stack

* **Python**
* **Pygame**
* **PyTorch** (for RL AI)
* **NumPy / Math**
* File handling for leaderboard system

---

##  Project Structure

```
├── arcade_shooter_full.py   # Main game
├── entities.py              # Player / bullet base entities
├── r1_enemy.py              # RL enemy logic
├── agent.py                 # DQN Agent
├── model.py                 # Neural Network
├── buffer.py                # Replay Buffer
├── train.py                 # RL training script
├── make_sound.py            # Sound generator
├── sounds/
├── leaderboard.txt
├── highscore.txt
```

---

##  How to Run

###  Clone the repo

```bash
git clone https://github.com/your-username/bullet-hell-shooter.git
cd bullet-hell-shooter
```

###  Install dependencies

```bash
pip install pygame torch
```

###  Run the game

```bash
python arcade_shooter_full.py
```

---

##  Train RL Enemy (Optional)

```bash
python train.py
```

This will train DQN agents using simulated combat.

---

##  Controls

| Key        | Action          |
| ---------- | --------------- |
| Arrow Keys | Move            |
| Space      | Shoot           |
| P          | Pause           |
| Mouse      | Menu Navigation |

---

##  Leaderboard System

* Scores saved locally
* High score tracking
* Player name input
* Animated leaderboard screen

---

##  Sound

Shooting sound generated programmatically:

Run if missing:

```bash
python make_sound.py
```

---

## Screenshots

*Add your gameplay screenshots here
<img width="1202" height="948" alt="Screenshot 2026-02-05 160635" src="https://github.com/user-attachments/assets/2fb52923-6516-4f4f-8981-22b4b3f28d1b" />
<img width="1202" height="948" alt="Screenshot 2026-02-05 160705" src="https://github.com/user-attachments/assets/9ae458c9-ce8d-4bb7-bbe2-78c35f14d270" />


---

## Future Improvements

* Online leaderboard
* Multiplayer mode
* Mobile port
* More boss mechanics
* Advanced RL training
*sprites

---

## Author

**Ankan Kumar Panja**
CSE Student | Game Dev | ML Enthusiast | Web Developer 

---

##

---

⭐ If you like this project, don’t forget to star the repo!
