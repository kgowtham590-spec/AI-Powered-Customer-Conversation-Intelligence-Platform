import logging

logger = logging.getLogger(__name__)


class DiarizationService:
    def __init__(self):
        logger.info("Using heuristic speaker diarization.")

    def diarize(self, audio_path: str, transcript_segments: list) -> list:
        if not transcript_segments:
            return []

        diarized_segments = []

        # Decide who starts the conversation
        first_text = transcript_segments[0]["text"].lower()

        advisor_keywords = [
            "thank you",
            "welcome",
            "my name is",
            "calling from",
            "fitnova",
            "good morning",
            "good afternoon",
            "good evening"
        ]

        if any(keyword in first_text for keyword in advisor_keywords):
            current_speaker = "Advisor"
        else:
            current_speaker = "Customer"

        short_responses = {
            "yes",
            "yeah",
            "yep",
            "ok",
            "okay",
            "sure",
            "right",
            "correct",
            "hello",
            "hi",
            "thanks",
            "thank you",
            "no"
        }

        for i, seg in enumerate(transcript_segments):

            if i > 0:
                previous = transcript_segments[i - 1]

                text = seg["text"].strip().lower()
                words = text.split()

                # Long pause → speaker change
                if seg["start"] - previous["end"] > 1.0:
                    current_speaker = (
                        "Customer"
                        if current_speaker == "Advisor"
                        else "Advisor"
                    )

                # Very short acknowledgements → speaker change
                elif len(words) <= 2 or text in short_responses:
                    current_speaker = (
                        "Customer"
                        if current_speaker == "Advisor"
                        else "Advisor"
                    )

                # Advisor introduction
                elif any(k in text for k in [
                    "my name is",
                    "calling from",
                    "thank you for calling",
                    "fitnova"
                ]):
                    current_speaker = "Advisor"

            diarized_segments.append({
                "start": seg["start"],
                "end": seg["end"],
                "speaker": current_speaker,
                "text": seg["text"]
            })

        logger.info(f"Diarized {len(diarized_segments)} segments.")

        return diarized_segments
