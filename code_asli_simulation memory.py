import numpy as np
import matplotlib.pyplot as plt

# Simulate memory formation
num_neurons = 100
learning_rate = 0.1
sensory_memory_capacity = 10
# Initialize the synaptic weights and neuron activations
weights = np.random.rand(num_neurons, num_neurons)
activations = np.random.rand(num_neurons)

# Simulate Hebbian learning
for i in range(1000):
  # Activate a random subset of neurons
  active_neurons = np.random.choice(num_neurons, size=10, replace=False)
  activations[active_neurons] = 1
  # Update the synaptic weights using STDP
  for j in range(num_neurons):
    for k in range(num_neurons):
      if activations[j] > 0 and activations[k] > 0:
        weights[j, k] += learning_rate * (1 - weights[j, k])
      elif activations[j] > 0 and activations[k] == 0:
        weights[j, k] -= learning_rate * weights[j, k]
  # Update the synaptic weights using the Hebbian learning rule
  weights += learning_rate * np.outer(activations, activations)
  
  # Reset the neuron activations
  activations = np.random.rand(num_neurons)

# Visualize the synaptic weights
plt.imshow(weights, cmap='hot', interpolation='nearest')
plt.title('Synaptic Weights after Hebbian Learning')
plt.show()
# Simulate memory consolidation
memory_strength = np.random.rand(100)  # Random memory strengths

memory_strength = np.convolve(memory_strength, np.ones(10)/10, mode='valid')

# Simulate memory retrieval
retrieval_strength = np.random.rand(100)  # Random retrieval strengths
sensory_memory = np.zeros((num_neurons, sensory_memory_capacity))
sensory_inputs = np.random.rand(num_neurons, 100)  # 100 time steps

# Visualize memory strengths over time
plt.plot(memory_strength)
plt.xlabel('Time')
plt.ylabel('Memory Strength')
plt.title('Memory Formation and Consolidation')
plt.show()

# Visualize retrieval strengths over time
plt.plot(retrieval_strength)
plt.xlabel('Time')
plt.ylabel('Retrieval Strength')
plt.title('Memory Retrieval')
plt.show()
# Simulate sensory memory
for t in range(100):
  # Add new sensory input to memory
  sensory_memory[:, t % sensory_memory_capacity] = sensory_inputs[:, t]
  
  # Decay existing memories
  sensory_memory *= (1 - learning_rate)

# Visualize sensory memory
plt.imshow(sensory_memory, cmap='hot', interpolation='nearest')
plt.xlabel('Time')
plt.ylabel('Sensory Input')
plt.title('Sensory Memory')
plt.show()
# Define brain regions and their connections
brain_regions = {
    'Hippocampus': {'connections': ['Amygdala', 'Prefrontal Cortex']},
    'Amygdala': {'connections': ['Hippocampus', 'Temporal Lobe']},
    'Prefrontal Cortex': {'connections': ['Hippocampus', 'Temporal Lobe', 'Basal Ganglia']},
    'Temporal Lobe': {'connections': ['Amygdala', 'Prefrontal Cortex', 'Auditory Cortex']},
    'Basal Ganglia': {'connections': ['Prefrontal Cortex', 'Motor Cortex']},
    'Auditory Cortex': {'connections': ['Temporal Lobe']},
    'Motor Cortex': {'connections': ['Basal Ganglia']}
}

# Define neural activity patterns for each region
neural_activity = {
    'Hippocampus': np.random.rand(100),  # 100 time steps
    'Amygdala': np.random.rand(100),
    'Prefrontal Cortex': np.random.rand(100),
    'Temporal Lobe': np.random.rand(100),
    'Basal Ganglia': np.random.rand(100),
    'Auditory Cortex': np.random.rand(100),
    'Motor Cortex': np.random.rand(100)
}

# Simulate neural activity propagation
def propagate_activity(region, time_step):
    if time_step < 99:  # Check if time_step is within bounds
        activity = neural_activity[region][time_step]
        for connected_region in brain_regions[region]['connections']:
            neural_activity[connected_region][time_step + 1] += activity * 0.5  # 50% transmission

# Simulate brain activity
for time_step in range(99):  # Iterate up to 99 to avoid index error
    for region in brain_regions:
        propagate_activity(region, time_step)

# Visualize brain activity
plt.figure(figsize=(10, 6))
for i, region in enumerate(brain_regions):
    plt.subplot(2, 4, i + 1)
    plt.plot(neural_activity[region])
    plt.title(region)
    plt.xlabel('Time')
    plt.ylabel('Neural Activity')
plt.tight_layout()
plt.show()
# Define neurotransmitters and hormones
neurotransmitters = {
    'Dopamine': {'release_rate': 0.1, 'decay_rate': 0.05},
    'Serotonin': {'release_rate': 0.2, 'decay_rate': 0.1},
    'Acetylcholine': {'release_rate': 0.3, 'decay_rate': 0.15}
}

hormones = {
    'Adrenaline': {'release_rate': 0.5, 'decay_rate': 0.2},
    'Insulin': {'release_rate': 0.4, 'decay_rate': 0.3}
}

# Initialize concentrations
neurotransmitter_concentrations = {nt: 0.0 for nt in neurotransmitters}
hormone_concentrations = {h: 0.0 for h in hormones}

# Simulate neurotransmitter and hormone release and decay
time_steps = 100
for t in range(time_steps):
    for nt, props in neurotransmitters.items():
        release_amount = props['release_rate'] * np.random.rand()
        decay_amount = props['decay_rate'] * neurotransmitter_concentrations[nt]
        neurotransmitter_concentrations[nt] += release_amount - decay_amount
    
    for h, props in hormones.items():
        release_amount = props['release_rate'] * np.random.rand()
        decay_amount = props['decay_rate'] * hormone_concentrations[h]
        hormone_concentrations[h] += release_amount - decay_amount

# Visualize concentrations over time
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
for nt, conc in neurotransmitter_concentrations.items():
    plt.plot([conc] * time_steps, label=nt)
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Neurotransmitters')
plt.legend()

plt.subplot(2, 1, 2)
for h, conc in hormone_concentrations.items():
    plt.plot([conc] * time_steps, label=h)
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Hormones')
plt.legend()

plt.tight_layout()
plt.show()