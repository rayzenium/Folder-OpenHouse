import numpy as np
from scipy.io import wavfile

sample_rate = 44100

def save_wave(filename, wave):
    # Apply a quick fade out to prevent audio popping at the end of the sound
    fade = np.linspace(1.0, 0.0, len(wave))
    wave = wave * fade
    wavfile.write(filename, sample_rate, np.int16(wave * 32767))

def generate_square_note(freq, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sign(np.sin(2 * np.pi * freq * t))

# 1. Hard Drop: Quick pitch sliding down (150Hz to 50Hz)
t_drop = np.linspace(0, 0.15, int(sample_rate * 0.15), endpoint=False)
drop_freqs = np.linspace(150, 50, len(t_drop))
hard_drop_wave = np.sign(np.sin(2 * np.pi * drop_freqs * t_drop))
save_wave('hard_drop.wav', hard_drop_wave)

# 2. Single Line Clear: Quick high beep (E5 note)
single_clear_wave = generate_square_note(659.25, 0.15)
save_wave('single_clear.wav', single_clear_wave)

# 3. 4-Block Clear (Tetris): Fast Arpeggio (C5 -> E5 -> G5 -> C6)
tetris_wave = np.concatenate([
    generate_square_note(523.25, 0.1),  # C5
    generate_square_note(659.25, 0.1),  # E5
    generate_square_note(783.99, 0.1),  # G5
    generate_square_note(1046.50, 0.3)  # C6 (held slightly longer)
])
save_wave('tetris_clear.wav', tetris_wave)

# 4. Game Over: Descending heavy tones
game_over_wave = np.concatenate([
    generate_square_note(250, 0.2),
    generate_square_note(200, 0.2),
    generate_square_note(150, 0.2),
    generate_square_note(100, 0.5)
])
save_wave('game_over.wav', game_over_wave)