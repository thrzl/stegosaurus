# 🦕stegosaurus
a steganography based discord bot, made with 💚 using 🐍

## 🔧 run it yourself
to run stegosaurus yourself, you need to have python 3.8+ installed. after downloading and extracting the files, navigate to the folder and use:
```sh
pip install -r requirements.txt # Linux

py -3 -m pip install -r requirements.txt # Windows
```

## 🏗 feature log
- [x] zero width character encoding/decoding
- [x] caesar ciphers
- [x] binary encoding
- [x] a1z26 encoding
- [ ] other types...

## 🥁 background

this bot was created to submit in [swas.py's bot jam](https://discord.gg/j3YzsdnRvx). once the topic (cryptography) was revealed, i immediately had my idea. i got to work, and well, here we are!

my initial idea for the bot was to use zero-width characters, as they were invisible, and as they aren't very well known about. they are traditionally used for foreign language scripts such as arabic so that a text editor or webpage would know to show them right-to-left, or that two characters are part of a different word. they weren't meant to be seen, so they have a width of zero, making them invisible (until you run the text caret over them.)
