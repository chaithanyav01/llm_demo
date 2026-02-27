import torch
import torch.nn as nn
import torch.nn.functional as F
from transformer_blocks import Block

# Create vocabulary (same as training)
corpus = [
    "hello friends how are you",
    "the tea is very hot", 
    "my name is Chaithanya",
    "the roads of Delhi are busy",
    "it is raining in Mumbai",
    "the train is late again",
    "i love eating samosas and drinking tea",
    "holi is my favorite festival",
    "diwali brings lights and sweets",
    "india won the cricket match"
]

corpus = [s + " <END>" for s in corpus]
text = " ".join(corpus)
words = list(set(text.split()))

vocab_size = len(words)
word2idx = {w: i for i, w in enumerate(words)}
idx2word = {i: w for w, i in word2idx.items()}

# Model definition
class TinyGPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding = nn.Embedding(vocab_size, 32)
        self.position_embedding = nn.Embedding(6, 32)
        self.blocks = nn.Sequential(*[Block(32, 6, 2) for _ in range(2)])
        self.ln_f = nn.LayerNorm(32)
        self.head = nn.Linear(32, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding(idx)
        pos_emb = self.position_embedding(torch.arange(T, device=idx.device))
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.head(x)
        loss = None
        if targets is not None:
            B, T, C = logits.shape
            loss = F.cross_entropy(logits.view(B*T, C), targets.view(B*T))
        return logits, loss

    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -6:]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            next_idx = torch.multinomial(probs, 1)
            idx = torch.cat((idx, next_idx), dim=1)
        return idx

# Load model
model = TinyGPT()
model.load_state_dict(torch.load("models/tiny_gpt.pt", map_location='cpu'))
model.eval()

# Inference function
def generate_text(prompt="hello", max_new_tokens=15):
    # Convert prompt to indices
    prompt_words = prompt.split()
    indices = [word2idx[w] for w in prompt_words if w in word2idx]
    if not indices:
        indices = [word2idx["hello"]]
    
    # Generate
    context = torch.tensor([indices], dtype=torch.long)
    with torch.no_grad():
        generated = model.generate(context, max_new_tokens)
    
    # Convert back to text
    result = " ".join([idx2word[int(i)] for i in generated[0]])
    return result

if __name__ == "__main__":
    prompt = "hello"
    generated_text = generate_text(prompt)
    print(f"Prompt: {prompt}")
    print(f"Generated text: {generated_text}")
