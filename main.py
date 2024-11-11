# main.py
from Class import MusicalNote, load_audio, save_audio, analyze_audio, apply_changes
from functions import sort_notes_by_tempo, sort_notes_by_loudness, sort_and_flag_notes

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
    notes = sort_and_flag_notes(notes)

    # Step 4: Apply changes to the audio
    print("Applying changes to audio...")
    y_modified = apply_changes(notes, y, sr)

    # Print all the notes that are present in the modified audio
    print("Notes in the modified audio:")
    for note in notes:
        print(note)

    # Step 5: Save the modified audio
    print("Saving modified audio...")
    save_audio(output_file_path, y_modified, sr)
    print(f"Modified audio saved to {output_file_path}")

if __name__ == "__main__":
    main()
