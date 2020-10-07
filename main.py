from res import transcriptor as tr
print("Transcriptor transform ru word to eng")
engine=input("Select engine, 1 - dictionary, 2 - if`s - ")
inp_word=input("Enter your word to transcript: ")
in_lang=input("Enter input language (ru or en): ")
out_lang=input("Enter output language (ru or en): ")
tr.transcript(in_lang, out_lang, inp_word, engine)