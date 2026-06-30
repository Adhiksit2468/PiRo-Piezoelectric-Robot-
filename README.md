# PiRo-Piezoelectric-Robot-

## Overview
PiRo is a conceptual underwater robotic fish exploring piezoelectric energy harvesting and supercapacitor-based storage as a supplementary energy system for low-power underwater robotics.

The goal is not full battery replacement, but investigation into **energy scavenging from underwater mechanical environments**.

---

## Inspiration
Inspired by MIT’s SoFi robotic fish, which operates using lithium batteries, PiRo explores whether ambient underwater motion and structural deformation can be partially converted into usable electrical energy to extend operational lifetime.

---

## Core Concept
PiRo embeds piezoelectric materials into a flexible robotic fish structure. These materials convert mechanical stress from:

- water flow  
- turbulence  
- body deformation  

into electrical energy.

### Key Relation:
Q = d × F

Where:
- Q = generated charge  
- d = piezoelectric coefficient  
- F = applied force  

Energy harvesting depends on **dynamic stress variation**, not static hydrostatic pressure.

---

## Energy System Architecture

Water Motion  
→ Mechanical Deformation  
→ Piezoelectric Conversion  
→ Rectification  
→ Supercapacitor Storage  
→ Low-Power Electronics  

---

## Engineering Constraints

### 1. Static Pressure Limitation
Hydrostatic pressure underwater is constant and does not produce usable electrical output.

### 2. Low Power Density
Typical output ranges:
- 0.01–0.1 W (piezoelectric harvesting)

Required propulsion:
- 1–10 W

---

### 3. Efficiency Losses
Total system efficiency is estimated at:
**~5% to 15%**

Losses occur in conversion, rectification, and storage stages.

---

## Energy Gap Challenge

There is a fundamental mismatch between:

- Energy harvested: 0.01–0.1 W  
- Energy required: 1–10 W  

This creates a **10×–100× power gap**.

---

## Supercapacitor Role
Supercapacitors are used only for:
- energy buffering  
- smoothing intermittent power  
- supporting low-power electronics  

They do not generate energy.

---

## System Interpretation
PiRo is best understood as:

> A hybrid underwater robotic system with energy-scavenging augmentation, not a self-powered propulsion system.

---

## Engineering Conclusion
PiRo demonstrates that piezoelectric energy harvesting is physically valid underwater but insufficient for continuous propulsion.

It is best suited for:
- low-power sensing systems  
- intermittent electronics  
- extending battery life rather than replacing it  

---

## Status
This project is currently in conceptual and analytical stage, focusing on physics feasibility and system-level constraints.
