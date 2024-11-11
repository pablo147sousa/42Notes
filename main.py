# main.py
from Class import MusicalNote, load_audio, save_audio, analyze_audio, apply_changes
def sort_and_limit_notes(notes, limit=42):
	# Sort notes by loudness in descending order
	sorted_notes = sorted(notes, key=lambda note: note.loudness, reverse=True)
	# Limit to the specified number of notes
	return sorted_notes[:limit]
def main():
    # Path to the input audio file
    input_file_path = "/home/pablo/Docs/42Cursus/42Projects/42Notes/42Notes/Giorno s Theme .mp3"  # Replace with your actual file path
    output_file_path = "Giorno modified.wav"  # Where to save the modified file

    # Step 1: Load audio
    print("Loading audio...")
    y, sr = load_audio(input_file_path)
    print(f"Audio loaded. Sample rate: {sr}, Duration: {len(y)/sr:.2f} seconds.")

    # Step 2: Analyze audio and create notes
    print("Analyzing audio to create notes...")
    notes = analyze_audio(y, sr)
    print(f"Detected {len(notes)} notes.")

    # Step 3: Modify notes
    print("Modifying notes...")
    for note in notes:
           notes = sort_and_limit_notes(notes)
        #note.adjust_loudness(0.1)  # Example: increase loudness
        #note.adjust_tempo(130)     # Example: change tempo to 130 BPM# Sort and limit notes

    # Step 4: Apply changes to the audio
    print("Applying changes to audio...")
    y_modified = apply_changes(notes, y, sr)

    # Step 5: Save the modified audio
    print("Saving modified audio...")
    save_audio(output_file_path, y_modified, sr)
    print(f"Modified audio saved to {output_file_path}")

if __name__ == "__main__":
    main()
