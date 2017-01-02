# Replay memory minimum and maximum size
MIN_MEM_SIZE, MAX_MEM_SIZE = 2400, 80000

# Batch size for NN ingestion
BATCH_SIZE = 32

# Sequence length for NN ingestion
SEQUENCE_LENGTH = 8

# Maximum episode duration, in frames
MAX_EPISODE_LENGTH = 125  # 500 with a frame skip of 4

# Number of training steps
TRAINING_STEPS = 1000

# Number of training steps
QLEARNING_STEPS = 1000

# Maximum number of cores to use
MAX_CPUS = 32

# Number of possible actions
N_ACTIONS = 8

# Learning rate for tensorflow optimizers
LEARNING_RATE = 0.00001

DEATH_PENALTY = 25
KILL_REWARD = 100
PICKUP_REWARD = 4

try:
    from local_config import * # NOQA
except ImportError:
    pass
