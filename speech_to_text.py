import whisper
import argparse
from pathlib import Path
import sys
parser = argparse.ArgumentParser(description ="Whisper Speech to Text CLI.")

parser.add_argument("-p", "--path",type=str, help ="Path to the Audio File. Supports WAV, MP3, Flac.", required=True)
parser.add_argument("-v", "--verbose", type=bool, default=False, help = "Whether to see progress of transciption.", required=False)
parser.add_argument("-s", "--save", type=bool,default=False, help="Whether to save the transcript or not.")
parser.add_argument("-f","--file_name", type=str,default="audio_transcript.txt",help="File name to which transcript is to be saved.", required=False)

args = parser.parse_args()

model = whisper.load_model("base")

result = model.transcribe(args.path,fp16=False, verbose=args.verbose)
if args.save is True:
    with open(args.file_name, "w+") as f:
        f.write(result["text"])
print(result["text"])


