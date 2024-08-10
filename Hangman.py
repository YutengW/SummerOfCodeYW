import random
lives = 9
words = ['about', 'alert', 'argue', 'beach', 'above', 'alike', 'arise', 'began', 'abuse', 'alive', 'array', 'begin', 'actor', 'allow', 'aside', 'begun', 'acute', 'alone', 'asset', 'being', 'admit', 'along', 'audio', 'below', 'adopt', 'alter', 'audit', 'bench', 'adult', 'among', 'avoid', 'billy', 'after', 'anger', 'award', 'birth', 'again', 'angle', 'aware', 'black', 'agent', 'angry', 'badly', 'blame', 'agree', 'apart', 'baker', 'blind', 'ahead', 'apple', 'bases', 'block', 'alarm', 'apply', 'basic', 'blood', 'album', 'arena', 'basis', 'board', 'boost', 'buyer', 'china', 'cover', 'booth', 'cable', 'chose', 'craft', 'bound', 'calif', 'civil', 'crash', 'brain', 'carry', 'claim', 'cream', 'brand', 'catch', 'class', 'crime', 'bread', 'cause', 'clean', 'cross', 'break', 'chain', 'clear', 'crowd', 'breed', 'chair', 'click', 'crown', 'brief', 'chart', 'clock', 'curve', 'bring', 'chase', 'close', 'cycle', 'broad', 'cheap', 'coach', 'daily', 'broke', 'check', 'coast', 'dance', 'brown', 'chest', 'could', 'dated', 'build', 'chief', 'count', 'dealt', 'built', 'child', 'court', 'death', 'debut', 'entry', 'forth', 'group', 'grown', 'guard', 'delay', 'equal', 'forty', 'happy', 'depth', 'error', 'forum', 'guess', 'doubt', 'event', 'found', 'guest', 'doing', 'every', 'frame', 'guide', 'dozen', 'exact', 'frank', 'harry', 'draft', 'exist', 'fraud', 'heart', 'drama', 'extra', 'fresh', 'heavy', 'drawn', 'faith', 'front', 'hence', 'dream', 'false', 'fruit', 'night', 'dress', 'fault', 'fully', 'horse', 'drill', 'fibre', 'funny', 'hotel', 'drink', 'field', 'giant', 'house', 'drive', 'fifth', 'given', 'human', 'drove', 'fifty', 'glass', 'ideal', 'dying', 'fight', 'globe', 'image', 'eager', 'final', 'going', 'index', 'early', 'first', 'grace', 'inner', 'earth', 'fixed', 'grade', 'input', 'eight', 'flash', 'grand', 'issue', 'elite', 'fleet', 'grant', 'irony', 'empty', 'floor', 'grass', 'juice', 'enemy', 'fluid', 'great', 'joint', 'enjoy', 'focus', 'green', 'judge', 'enter', 'force', 'gross', 'known', 'label', 'metal', 'media', 'newly', 'local', 'might', 'noise', 'north', 'logic', 'minor', 'noted', 'novel', 'large', 'loose', 'minus', 'nurse', 'laser', 'lower', 'mixed', 'occur', 'later', 'lucky', 'model', 'ocean', 'laugh', 'lunch', 'money', 'offer', 'layer', 'lying', 'month', 'often', 'learn', 'magic', 'moral', 'order', 'lease', 'major', 'motor', 'other', 'least', 'maker', 'mount', 'ought', 'leave', 'march', 'mouse', 'paint', 'legal', 'music', 'mouth', 'paper', 'level', 'match', 'movie', 'party', 'light', 'mayor', 'needs', 'radio', 'panel', 'press', 'raise', 'route', 'phase', 'price', 'range', 'royal', 'phone', 'pride', 'rapid', 'rural', 'photo', 'prime', 'ratio', 'scale', 'piece', 'print', 'reach', 'scene', 'pilot', 'prior', 'ready', 'scope', 'pitch', 'prize', 'refer', 'score', 'place', 'proof', 'right', 'sense', 'plain', 'proud', 'rival', 'serve', 'plane', 'prove', 'river', 'seven', 'plant', 'queen', 'quick', 'shall', 'plate', 'sixth', 'stand', 'shape', 'point', 'quiet', 'roman', 'share', 'pound', 'quite', 'rough', 'sharp', 'sheet', 'spare', 'style', 'times', 'shelf', 'speak', 'sugar', 'tired', 'shell', 'speed', 'suite', 'title', 'shift', 'spend', 'super', 'today', 'shirt', 'spent', 'sweet', 'topic', 'shock', 'split', 'table', 'total', 'shoot', 'spoke', 'taken', 'touch', 'short', 'sport', 'taste', 'tough', 'shown', 'staff', 'taxes', 'tower', 'sight', 'stage', 'teach', 'track', 'since', 'stake', 'teeth', 'trade', 'sixty', 'start', 'texas', 'treat', 'sized', 'state', 'thank', 'trend', 'skill', 'steam', 'theft', 'trial', 'sleep', 'steel', 'their', 'tried', 'slide', 'stick', 'theme', 'tries', 'small', 'still', 'there', 'truck', 'smart', 'stock', 'these', 'truly', 'smile', 'stone', 'thick', 'trust', 'smith', 'stood', 'thing', 'truth', 'smoke', 'store', 'think', 'twice', 'solid', 'storm', 'third', 'under', 'solve', 'story', 'those', 'undue', 'sorry', 'strip', 'three', 'union', 'sound', 'stuck', 'threw', 'unity', 'south', 'study', 'throw', 'until', 'space', 'stuff', 'tight', 'upper', 'upset', 'whole', 'waste', 'wound', 'urban', 'whose', 'watch', 'write', 'usage', 'woman', 'water', 'wrong', 'usual', 'train', 'wheel', 'wrote', 'valid', 'world', 'where', 'yield', 'value', 'worry', 'which', 'young', 'video', 'worse', 'while', 'youth', 'virus', 'worst', 'white', 'worth', 'visit', 'would', 'vital', 'voice']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives Left: ' + heart_symbol * lives)
    guess = input('guess a letter or the whole word: ')
    
    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect, you lose a life')
        lives = lives - 1
    
if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word + '!')
else:
    print('You lost! The secret word was ' + secret_word + '!')