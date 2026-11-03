"""Narrate the shorts in a designed explainer voice with VoxCPM2 (the YouTube project's local install), one file per line.

  "$HOME/Projects/Youtube Channel/voice/env/.venv/bin/python" voice.py <short> [<short> ...]
  ... voice.py --test "<line>"          one line in the voice, to tests/voice-test.wav

No reference recording: the voice comes from VOICE, a written description VoxCPM2 designs a voice from.
Writes voice/<short>/NN.wav and voice/<short>/lines.json (text, file, seconds). A fixed seed per line keeps
the voice and every take the same on a re-run. Heavy job: run nothing else heavy on the Mac at the same time.
"""
import json, pathlib, subprocess, sys, os
import soundfile as sf
import torch
from huggingface_hub import snapshot_download
from voxcpm import VoxCPM

HERE = pathlib.Path(__file__).parent
VOICE = ("A clear, warm British woman in her thirties explaining how something works to a friend: "
         "unhurried, confident, friendly, plain speech, no drama")
REV = "32279effe8c19989596f05d353d1447f51d9e915"   # the VoxCPM2 weights the YouTube project pinned
SEED = 7

subprocess.Popen(["caffeinate", "-i", "-w", str(os.getpid())])
model = VoxCPM.from_pretrained(snapshot_download("openbmb/VoxCPM2", revision=REV), load_denoiser=False)
SR = model.tts_model.sample_rate


def say(text, out):
    torch.manual_seed(SEED)
    wav = model.generate(text=f"({VOICE}){text}", cfg_value=2.0, inference_timesteps=10)
    sf.write(out, wav, SR)
    return round(len(wav) / SR, 2)


def lines(script, end):
    return [*script["sparse"], *script["sketch"], *[o[0] for o in script["objects"]], *script["colour"], end]


if sys.argv[1] == "--redo":                          # --redo <short> <line> <seed>: a new take of one line
    short, i, seed = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    d = HERE / "voice" / short
    rec = json.loads((d / "lines.json").read_text())
    SEED = seed
    rec[i]["seconds"], rec[i]["seed"] = say(rec[i]["text"], d / rec[i]["file"]), seed
    (d / "lines.json").write_text(json.dumps(rec, indent=1) + "\n")
    print(short, i, rec[i]["seconds"], "s, seed", seed)
    sys.exit()

if sys.argv[1] == "--test":
    (HERE / "tests").mkdir(exist_ok=True)
    print(say(sys.argv[2], HERE / "tests" / "voice-test.wav"), "s")
    sys.exit()

scripts = json.loads((HERE / "scripts.json").read_text())
for short in sys.argv[1:]:
    d = HERE / "voice" / short
    d.mkdir(parents=True, exist_ok=True)
    out = []
    for i, text in enumerate(lines(scripts[short], scripts["_end"])):
        f = d / f"{i:02d}.wav"
        out.append(dict(text=text, file=f.name, seconds=say(text, f)))
        print(short, i, out[-1]["seconds"], "s", flush=True)
    (d / "lines.json").write_text(json.dumps(out, indent=1) + "\n")
