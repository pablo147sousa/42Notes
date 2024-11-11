def sort_notes_by_loudness(notes):
	# Sort notes by loudness in descending order
	sorted_notes = sorted(notes, key=lambda note: note.loudness, reverse=True)
	return sorted_notes

def sort_notes_by_tempo(notes):
	# Sort notes by tempo (beats) in descending order
	sorted_notes = sorted(notes, key=lambda note: note.tempo, reverse=True)
	return sorted_notes

def sort_and_flag_notes(notes, limit=42):
	# Sort notes by loudness in descending order
	notes = sort_notes_by_loudness(notes)
	notes = sort_notes_by_tempo(notes)
	# Flag all notes beyond the top 'limit' for deletion
	for note in notes[limit:]:
		note.delete = True
	return notes

def calculate_weighted_average_tempo(notes):
	total_weight = sum(note.loudness for note in notes)
	weighted_sum = sum(note.tempo * note.loudness for note in notes)
	weighted_average = weighted_sum / total_weight if total_weight != 0 else 0
	return weighted_average
