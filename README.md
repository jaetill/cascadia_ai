# 🌲 Cascadia AI — A Modular Game Agent for Tile-Laying Strategy

Welcome to Cascadia AI, a Python-based exploration of game agent behavior in the award-winning board game *Cascadia*. This project aims to simulate decision-making, board evaluation, and drafting logic for both human and AI players in a modular, extensible system.

---

## 🎯 Project Goals

- Model the core rules and spatial logic of Cascadia in Python
- Implement multiple AI agents with varying levels of sophistication:
  - Greedy scorer
  - Goal-pattern maximizer
  - Adaptive or opponent-aware AI
- Provide a clean CLI interface with future UI hooks
- Maintain a modular architecture that supports testing, replay simulation, and AI experimentation

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Editor**: VS Code (recommended)
- **Architecture**: MVC-style modular breakdown with separate layers for game logic, AI, and interface
- **Future Add-ons**:
  - Visual UI (Tkinter or Pygame)
  - AI vs. AI auto-battler
  - Player replay logging

---

## 🚀 Getting Started

```bash
git clone https://github.com/jaetill/cascadia_ai.git
cd cascadia_ai
python main.py
