import librosa
import numpy as np
import soundfile as sf

class MusicalNote:
    def __init__(self, note_id, loudness=0.0, tempo=120.0):
        """
        Initialize a musical note.
        Parameters:
        - note_id (int): Unique identifier for the note
        - loudness (float): Loudness of the note
        - tempo (float): Tempo of the note in BPM
        """
        self.id = note_id
        self.loudness = loudness
        self.tempo = tempo
    
    def adjust_loudness(self, delta):
        """Adjust the loudness of the note by a delta value."""
        self.loudness += delta

    def adjust_tempo(self, new_tempo):
        """Set a new tempo for the note."""
        self.tempo = new_tempo

    def __str__(self):
        return f"Note ID: {self.id}, Loudness: {self.loudness}, Tempo: {self.tempo}"

def load_audio(file_path):
    """
    Load an audio file using librosa.
    Returns the audio signal and sample rate.
    """
    y, sr = librosa.load(file_path, sr=None)
    return y, sr

def save_audio(file_path, y, sr):
    """
    Save an audio signal to a file.
    """
    sf.write(file_path, y, sr)

def analyze_audio(y, sr):
    """
    Analyze audio features such as tempo and loudness.
    Returns a list of MusicalNote instances based on detected beats.
    """
    # Estimate tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    # Get loudness for each beat frame
    rms = librosa.feature.rms(y=y)
    
    # Identify beat frames
    beat_frames = librosa.beat.beat_track(y=y, sr=sr, units='time')[1]
    
    notes = []
    for idx, beat_time in enumerate(beat_frames):
        note = MusicalNote(note_id=idx, loudness=rms[0, idx], tempo=tempo)
        notes.append(note)
    
    return notes

def apply_changes(notes, y, sr):
    """
    Modify the audio based on note changes and return modified signal.
    """
    # Example: Apply tempo change to the entire signal if needed
    tempo_changes = np.array([note.tempo for note in notes])
    
    # Resample if any tempo changes have been applied (simplification)
    # Adjust based on average tempo if needed
    new_y = librosa.effects.time_stretch(y, rate=np.mean(tempo_changes)/120.0)  # assuming 120 BPM as base tempo
    
    # Apply loudness changes based on notes (simplification example)
    rms_loudness = np.array([note.loudness for note in notes])
    target_rms = np.mean(rms_loudness)
    if target_rms > 0:
        new_y = new_y * (target_rms / np.sqrt(np.mean(new_y**2)))
    
    return new_y

# Usage
file_path = "/home/pablo/Docs/42Cursus/42Projects/42Notes/42Notes/Giorno s Theme .mp3"
y, sr = load_audio(file_path)

# Analyze audio to get note features
notes = analyze_audio(y, sr)

# Make some adjustments to notes
for note in notes:
    note.adjust_loudness(0.1)  # Increase loudness by 0.1 for each note
    note.adjust_tempo(130)     # Set tempo to 130 BPM for each note

# Apply changes to audio
y_modified = apply_changes(notes, y, sr)

# Save modified audio
print("Original Notes:")
for note in notes:
	print(note)

# Apply changes to audio
y_modified = apply_changes(notes, y, sr)

# Save modified audio
output_file_path = "/home/pablo/Docs/42Cursus/42Projects/42Notes/42Notes/Giorno_s_Theme_modified.mp3"
save_audio(output_file_path, y_modified, sr)

print("Modified audio saved successfully.")