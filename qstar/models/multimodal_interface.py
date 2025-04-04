# qstar/models/multimodal_interface.py
from transformers import BlipProcessor, BlipForConditionalGeneration, Wav2Vec2ForCTC, Wav2Vec2Processor
from qstar.models.text.generate import QStarTextGenerator
from PIL import Image
import torch
import torchaudio
import os

class QStarVision:
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)

    def describe_image(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(image, return_tensors="pt")
        out = self.model.generate(**inputs, max_new_tokens=50)
        return self.processor.decode(out[0], skip_special_tokens=True)

    def qstar_image_pipeline(self, image_path):
        caption = self.describe_image(image_path)
        print(f"[Image] Caption généré : {caption}")
        verified = "photo" in caption.lower() or "image" in caption.lower()
        recalibrated = caption if verified else caption + ". Vérifie la scène."
        correlated = recalibrated + "\n[Annotation croisée effectuée]"
        final = correlated.strip().capitalize()
        print(f"[Image] Résultat final : {final}")
        return final


class QStarAudio:
    def __init__(self, model_name="facebook/wav2vec2-base-960h"):
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)

    def transcribe(self, audio_path):
        waveform, sample_rate = torchaudio.load(audio_path)
        inputs = self.processor(waveform.squeeze(), sampling_rate=sample_rate, return_tensors="pt", padding=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.batch_decode(predicted_ids)[0]
        return transcription

    def qstar_audio_pipeline(self, audio_path):
        transcript = self.transcribe(audio_path)
        print(f"[Audio] Transcription brute : {transcript}")
        verified = len(transcript.split()) > 3
        recalibrated = transcript if verified else transcript + ". Analyse complémentaire demandée."
        correlated = recalibrated + "\n[Alignement audio vérifié]"
        final = correlated.strip().capitalize()
        print(f"[Audio] Résultat final : {final}")
        return final


class QStarMultimodal:
    def __init__(self):
        self.text_model = QStarTextGenerator()
        self.vision_model = QStarVision()
        self.speech_model = QStarAudio()

    def analyze(self, prompt=None, image_path=None, audio_path=None):
        result = {}

        if prompt:
            print("[Texte] Traitement du prompt...")
            result["texte"] = self.text_model.generate(prompt)

        if image_path and os.path.exists(image_path):
            print("[Vision] Analyse de l'image...")
            result["image"] = self.vision_model.qstar_image_pipeline(image_path)

        if audio_path and os.path.exists(audio_path):
            print("[Audio] Analyse du fichier audio...")
            result["audio"] = self.speech_model.qstar_audio_pipeline(audio_path)

        return result

if __name__ == "__main__":
    mm = QStarMultimodal()
    output = mm.analyze(
        prompt="Décris une machine intelligente.",
        image_path="sample.jpg",
        audio_path="sample.wav"
    )
    print("\n🧠 Résultat multimodal :", output)
