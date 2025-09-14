print("Hello world!")
data = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon",
    "ability", "balance", "challenge", "decision", "effort", "freedom", "growth", "happiness", "inspiration", "journey",
    "knowledge", "learning", "motivation", "nature", "opportunity", "progress", "quality", "respect", "success", "teamwork",
    "understanding", "victory", "wisdom", "xenial", "youth", "zeal", "adventure", "bravery", "curiosity", "determination",
    "enthusiasm", "friendship", "gratitude", "honesty", "imagination", "joy", "kindness", "love", "mindfulness", "nurture",
    "optimism", "patience", "question", "resilience", "sincerity", "trust", "unity", "virtue", "warmth", "x-factor",
    "yearning", "zest", "active", "bold", "creative", "diligent", "energetic", "fearless", "generous", "hopeful",
    "intelligent", "jovial", "keen", "lively", "mindful", "noble", "outgoing", "persistent", "quick-witted", "reliable",
    "strong", "thoughtful", "unique", "versatile", "witty", "xenophobic", "young", "zealous", "ambitious", "brilliant"
]
group_count = 8
groups = [list() for _ in range(group_count)] #Utworzyliście listę zawierającą puste listy.

def hash_function(word):
    return sum(ord(letter) for letter in word)              #The ord() function returns the number representing the unicode code of a specified character.

for word in data:                       #Iterujemy po każdym słowie
    hash_sum = hash_function(word)
    group = hash_sum % group_count
    groups[group].append(word)

