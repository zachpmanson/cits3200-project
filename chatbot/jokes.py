#why so serious?
import random

dadjokes = [
    "I'm afraid for the calendar. Its days are numbered.",
    "Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!",
    "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
    "What did the ocean say to the beach?" "Nothing, it just waved.",
    "Why do seagulls fly over the ocean?" "Because if they flew over the bay, we'd call them bagels.",
    "Did you hear the rumor about butter? Well, I'm not going to spread it!",
    "I don't trust stairs. They're always up to something.",
    "What did one hat say to the other?" "Stay here! I'm going on ahead.",
    "Dad, can you put my shoes on?" "No, I don't think they'll fit me.",
    "What kind of car does an egg drive?" "A yolkswagen.",
    "How do you make 7 even?" "Take away the s.",
    "Why didn't the skeleton climb the mountain?" "It didn't have the guts.",
    "What time did the man go to the dentist? Tooth hurt-y.",
    "How many tickles does it take to make an octopus laugh? Ten tickles.",
    "Why did the math book look so sad? Because of all of its problems!",
    "If a child refuses to nap, are they guilty of resisting a rest?",
    "I'm on a seafood diet. I see food and I eat it.",
    "I made a pencil with two erasers. It was pointless.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "How did Harry Potter get down the hill?" "Walking. JK! Rowling.",
    "What's the best smelling insect?" "A deodor-ant.",
    "Did you hear about the guy who invented the knock-knock joke? He won the 'no-bell' prize.",
    "How do you make a Kleenex dance? Put a little boogie in it!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Have you ever tried to catch a fog? I tried yesterday but I mist.",
    ]

adultjokes = [
    "My mom died when we couldn’t remember her blood type. As she died, she kept telling us to “be positive,” but it’s hard without her.",
    "Today, I asked my phone “Siri, why am I still single?” and it activated the front camera.",
    "Why is it that if you donate a kidney, people love you. But if you donate five kidneys, they call the police.",
    "Dark humor is like food. Not everyone gets it.",
    "You don’t need a parachute to go skydiving. You need a parachute to go skydiving twice.,",
    "The doctor gave me one year to live, so I shot him with my gun. The judge gave me 15 years. Problem solved.",
    "My senior relatives liked to tease me at weddings, saying things like, “You’ll be next!” They stopped once I started doing the same to them at funerals.",
    "Son: Dad, did you get the results of the DNA test back? Dad: Call me George.",
    "If you were born in September, it's pretty safe to assume that your parents started their new year with a bang.",
    "Option 1: Let’s eat grandma. Option 2: Let’s eat, grandma. There you have it. Proof that punctuation saves lives.",
    "When does a joke become a dad joke? When it leaves you and never comes back.",
    "I bought my blind friend a cheese grater for his birthday. He later told me it was the most violent book he’d ever read.",
    "I tried to warn my son about playing Russian roulette. It went in one ear and out the other.",
    "They laughed at my crayon drawing. I laughed at their chalk outline.",
    "My wife and I have reached the difficult decision that we do not want children. If anybody does, please just send me your contact details and we can drop them off tomorrow.",
    '"I work with animals," the guy says to his date.  "That is so sweet," she replies. "I love a man who cares about animals. Where do you work?" "I am a butcher," he says.',
    "I have a joke about trickle down economics. But '99%' of you will never get it.",
    "Give a man a match, and he’ll be warm for a few hours. Set him on fire, and he will be warm for the rest of his life.",
    "Why can’t orphans play baseball? They don’t know where home is.",
    "My girlfriend, who’s into astronomy, asked me how stars die. “Usually an overdose,” I told her.",
    "I was at the park the other day when a mother sat down beside me. After a while, she leaned over and asked, “Which one is yours?”I looked at her and said, “I haven’t decided yet.”",
    "I want to die peacefully in my sleep, just like my grandfather. Not screaming like the passengers in his car.",
    "A man went into a library and asked for a book on how to commit suicide. The librarian said: “I can't, you won’t bring it back.",
    "What is the worst combination of illnesses? Alzheimer’s and diarrhea. You’re running but can’t remember where.",
    "They say there’s a person capable of murder in every friendship group. I suspected it was Dave, so I killed him before he could cause any harm.",
    ]

riddles = [ "What has to be broken before you can use it? Answer: An egg",
"I’m tall when I’m young, and I’m short when I’m old. What am I? Answer: A candle",
"What month of the year has 28 days? Answer: All of them",
"What is full of holes but still holds water? Answer: A sponge",
"What question can you never answer yes to? Answer: Are you asleep yet?",
"What is always in front of you but can’t be seen? Answer: The future",
"There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs? Answer:There aren’t any—it’s a one-story house.",
"What can you break, even if you never pick it up or touch it?Answer: A promise",
"What goes up but never comes down? Answer: Your age",
"What gets wet while drying? Answer: A towel",
"I shave every day, but my beard stays the same. What am I? Answer: A barber",
"You see a boat filled with people, yet there isn’t a single person on board. How is that possible? Answer: All the people on the boat are married.",
"I have branches, but no fruit, trunk or leaves. What am I? Answer: A bank",
"Two fathers and two sons are in a car, yet there are only three people in the car. How? Answer: They are a grandfather, father and son.",
"",
"",
"",
"",
"",


]

all_jokes = {
    'dadjokes': dadjokes,
    'adultjokes': adultjokes,
}

class typeofjokeNotFoundError(Exception):
    pass

def gets_jokes(categoryofjoke='dadjokes'):
    if categoryofjoke not in all_jokes:
        raise typeofjokeNotFoundError('The category of joke %s was not found' % (categoryofjoke))
    return all_jokes[categoryofjoke]

def obtain_joke(categoryofjoke):
    all_jokes = gets_jokes(categoryofjoke)
    return random.choice(all_jokes)


