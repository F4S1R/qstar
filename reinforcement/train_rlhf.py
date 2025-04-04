# train_rlhf.py
from trl import PPOTrainer, PPOConfig
from transformers import AutoTokenizer, AutoModelForCausalLM
from qstar.core import QStarVerifier
import torch

# Configuration PPO
config = PPOConfig(
    model_name="gpt2",
    batch_size=4,
    learning_rate=1e-5,
    log_with=None  # Peut être remplacé par "wandb" si nécessaire
)

# Modèle et tokenizer
model = AutoModelForCausalLM.from_pretrained(config.model_name)
tokenizer = AutoTokenizer.from_pretrained(config.model_name)

# Fonction de récompense personnalisée utilisant Q-STAR
verifier = QStarVerifier()

def reward_fn(prompt, response):
    score = verifier.score(prompt, response)  # Évalue la cohérence ou vérité contextuelle
    penalty = 0.2 if verifier.detect_hallucination(response) else 0.0
    return score - penalty

# Initialisation du PPOTrainer
ppo_trainer = PPOTrainer(
    config=config,
    model=model,
    tokenizer=tokenizer,
    reward_fn=reward_fn
)

# Jeu de données de démonstration
sample_prompts = [
    "Décris les symptômes de la grippe",
    "Quels sont les effets du réchauffement climatique?"
]

# Entraînement
for prompt in sample_prompts:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    generation = model.generate(input_ids, max_new_tokens=100)
    response = tokenizer.decode(generation[0], skip_special_tokens=True)

    reward = reward_fn(prompt, response)
    ppo_trainer.step([prompt], [response], [reward])
    print(f"Prompt : {prompt}\nRéponse : {response}\nRécompense : {reward}\n")
