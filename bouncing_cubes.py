"""
Bouncing Cubes animation script
For MIDIAnimator version 1.0
Licensed under the GNU General Public License v3.0

Notes:
Run script by pressing the "Run Script" button.
It will take 18-20 seconds to process. Be patient while MIDIAnimator processes the MIDI file & animates it.
"""

import bpy
from MIDIAnimator.data_structures.midi import MIDIFile
from MIDIAnimator.src.animation import MIDIAnimatorNode

# Get MIDI File
file = MIDIFile("//mapleaf.mid")

# Find both tracks and merge them
lh = file.findTrack('Piano - L.H.')
rh = file.findTrack('Piano - R.H.')
piano = file.mergeTracks(lh, rh, name="Piano")

# Assigning notes to objects
# You can also handle this in the 3D Viewport MIDAnimator menu.

scene = bpy.context.scene
scene.midi.quick_note_number_list = str(piano.allUsedNotes())
scene.midi.quick_obj_col = bpy.data.collections['Cubes']
scene.midi.quick_sort_by_name = True
bpy.ops.scene.quick_add_props()

for obj in bpy.data.collections['Cubes'].all_objects:
    obj.midi.note_on_curve = bpy.data.objects['ANIM_Osc']

# create a MIDIAnimatorNode object & add tracks
animator = MIDIAnimatorNode()
animator.addInstrument(instrumentType="evaluate", midiTrack=piano, objectCollection=bpy.data.collections['Cubes'])
animator.animate()
