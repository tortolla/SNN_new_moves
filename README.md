# Local, Bio-Inspired SNN (Adapted from Diehl & Cook 2015)
The idea for this repository comes from a **ready-made article** by **Diehl & Cook (2015)**,  
["Unsupervised learning of digit recognition using spike-timing-dependent plasticity."](https://doi.org/10.3389/fncom.2015.00099)  
We re-implemented their **Spiking Neural Network (SNN)** in **Brian2** and adapted it to a custom dataset of moving geometric shapes.  

**Author Contact:** [ivanov.fl@physicis.msu.ru](mailto:ivanov.fl@physicis.msu.ru) — Feel free to reach out for help or consultation if you want to run the code, tweak the parameters, or adapt it to your own data.

---

## Highlights
1. **Local Learning (STDP):**  
   - Synapses update based on local spike timing, emulating the human brain's biology.  
   - This local, event-driven plasticity is more **energy-efficient** and ideal for neuromorphic hardware.
2. **Dataset**  
   - In our setup, we used a **large** dataset of **moving shapes** (circles, squares, triangles) with different movements.  
   - **Due to size constraints, we cannot include it here**.  
   - **You can load your own data** by editing file paths and parameters in the code (explained below).  
   - Our version gets around **60%** accuracy; with tuning, you may get better results.
3. **Brian2 Framework**  
   - Leveraged for ease of coding spiking neurons, synapses, STDP rules, etc.
4. **Unsupervised Approach**  
   - No global labels or backpropagation are needed, only local spike-timing rules.  
   - After training, you assign a class label to each neuron by observing its activity patterns.


> **Important**: The `train/` and `test/` folders are empty because we cannot provide our large dataset.  
> Place your own images or frames into those folders (or rename them), then change paths in `utils.py` or wherever data is loaded.

---

## Installation

1. **Python 3.x**  
2. **Install Brian2**  
   ```bash
   pip install brian2



