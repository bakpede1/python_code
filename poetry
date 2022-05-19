print("Welcome to Poem Analyzer")
essay = "Offering: "
PARAGRAPH = "\n\n"
PROMPTS = []
prompt_count = 0

# title of analysis
title = input("Poem title: ")
essay = essay + title + PARAGRAPH

# body of analysis - 1
author = input("Author's name: ")
summary = input("Summary (Who? What? When? Purpose?, etc.): \n") + '.'
structure = input("How is the poem organized? \n") + '.'
stanza_count = int(input("How many stanzas: "))

# additional topics of essay
word_choice = input("What specific words does the author use to elicit emotion:\n ")
word_effect = input("What is the effect?\n ")
imagery = input("What image is painted:\n ") 
fig_lang = input("What fig, lang. is used & how it does it affect the poem:\n") + '.'

# add data to essay 
essay = essay + f'{title} written by {author} is a poem about ' + summary + structure + PARAGRAPH + word_choice + word_effect + PARAGRAPH + fig_lang

# stanza analysis
for i in range(stanza_count):
  print("Stanza " + str(i) + "\n")
  main_idea_for_stanza = input("Main idea  of stanza\n")
  quote = input("Supporting quote in stanza " + str(i) + ":\n")
  explanation_of_quote = input('Effect of quote in the poem:\n ')
  essay = essay + PARAGRAPH + main_idea_for_stanza + quote + explanation_of_quote

theme_tone = input("Takeway (the poet's overall message)? Poet's atttitude:\n ")
essay = essay + theme_tone

print(f'Here is the finished poem analysis for {title}\n------------------------')
print(essay)
print('------------------------')

