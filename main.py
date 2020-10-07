from res import transcriptor as tr

print("Transcriptor transform ru word to eng")
inp_word=str(input("Enter your word to transcript: "))
in_lang=str(input("Enter input language (ru or en): "))
out_lang=str(input("Enter output language (ru or en): "))

print("Result: "+tr.transcript(in_lang, out_lang, inp_word))