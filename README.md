# PiRo (Piezoelectric Robot)

PiRo is a conceptual underwater robotic fish exploring piezoelectric energy harvesting as an auxiliary power mechanism for low-power marine robotics.

The project investigates whether mechanical energy from fluid motion and structural deformation can be partially converted into electrical energy and stored in supercapacitors to extend operational lifetime of autonomous underwater systems.

---

## Key Idea

Water motion → mechanical deformation → piezoelectric conversion → rectification → supercapacitor storage → low-power electronics

---

## Core Objective

To evaluate piezoelectric energy harvesting as a **battery-assist system**, not a replacement, in underwater robotic applications.

---

## System Overview

![System Diagram](assets/piro_system.png)

---

## Key Physical Constraints

- Hydrostatic pressure does not generate usable electrical output
- Piezoelectric output is extremely low (µW–mW range)
- Propulsion requires significantly higher power (W range)
- Energy conversion losses reduce overall efficiency

---

## Key Equation

Q = d × F

E = ½ C V²

---

## Repository Structure

- `concept.md` → Full technical explanation
- `assets/` → System diagrams and visuals
- `simulations/` →  Python energy harvesting model
- `cad/` →  mechanical concept and annotated layout
- `results/` → simulation output graphs

---

## Status

Conceptual design, analytical modelling, and preliminary computational simulation completed.

---

## Results

### Piezoelectric Power Output
![Power Output](results/power_output.png)

### Energy Storage (Supercapacitor Model)
![Energy Storage](results/energy_storage.png)

## PiRo Internal System Layout

![PiRo Internal Layout](cad/PiRo_labelled_design.png)

## Future Work

- Physical prototype
- Waterproof housing
- Experimental validation
- CFD analysis
- Embedded electronics testing
