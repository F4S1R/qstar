# reward_fn.py
from qstar.core import QStarVerifier

verifier = QStarVerifier()

def score_response(prompt: str, response: str) -> float:
    """
    Retourne un score de cohérence basé sur les règles internes Q-STAR
    """
    return verifier.score(prompt, response)

def detect_hallucination(response: str) -> bool:
    """
    Détecte les hallucinations ou incohérences majeures dans la réponse
    """
    return verifier.detect_hallucination(response)

def composite_reward(prompt: str, response: str) -> float:
    """
    Combine le score et la pénalité pour produire la récompense finale
    """
    penalty = 0.2 if detect_hallucination(response) else 0.0
    return score_response(prompt, response) - penalty