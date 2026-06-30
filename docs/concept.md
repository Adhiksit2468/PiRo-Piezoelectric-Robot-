# PiRo (Piezoelectric Robot) – Technical Compilation
# 1. Introduction
PiRo is a conceptual underwater robotic fish exploring piezoelectric energy harvesting and supercapacitor-based storage as an alternative to conventional battery-driven underwater robots. The goal is not full replacement of batteries, but investigation into energy scavenging from underwater mechanical environments.
# 2. Origin
Inspired by MIT’s SoFi robotic fish, which operates using lithium batteries, PiRo explores whether environmental mechanical stress and fluid dynamics can be partially converted into usable electrical energy to extend operational lifetime of low-power underwater robotic systems.
# 3. Core Concept
PiRo uses piezoelectric materials embedded in its structure to convert mechanical stress from water flow, turbulence, and body deformation into electrical energy. This energy is conditioned and stored in supercapacitors to support sensors and low-power control systems.
## Key equation:
Q = d × F  (piezoelectric charge relation)
Energy harvesting depends on change in stress, not static hydrostatic pressure.



# 4. Energy System Architecture
Water motion → mechanical deformation → piezoelectric conversion → rectification → supercapacitor storage → low-power electronics
 
# 5. Major Physical Constraints to be solved:

#### 5.1 Static pressure limitation: Hydrostatic pressure is constant underwater, so it does not generate continuous electrical output.
#### 5.2 Low power density: Typical piezoelectric harvesters generate micro-watt to milli-watt scale power, insufficient for propulsion.
#### 5.3 Efficiency losses: Energy conversion, rectification, storage, and motor inefficiencies significantly reduce usable output.
Efficiency estimate:
Total efficiency ≈ 5% to 15% in realistic systems.

# 6. Energy vs Propulsion Mismatch

Typical propulsion systems require 1–10 W, while piezoelectric harvesting provides ~0.01–0.1 W under realistic conditions. This creates a 10×–100× energy gap.
# 7. Supercapacitor Limitation
Supercapacitors store limited energy and do not generate power. They can buffer energy but cannot sustain continuous propulsion without an external or primary energy source.
Energy formula:
E = (1/2)CV^2

# 8. Corrected Interpretation
PiRo is best understood as a hybrid energy-assisted underwater robot, where piezoelectric harvesting extends battery life rather than replaces it entirely.
# 9. Engineering Conclusion
The system is physically feasible as an energy scavenging enhancement layer but not as a standalone perpetual energy system. It can support low-power sensing and intermittent operation, not continuous propulsion.

## System Architecture Diagram

![PiRo System Architecture](https://raw.githubusercontent.com/Adhiksit2468/PiRo-Piezoelectric-Robot-/main/assets/piro_system.png)
