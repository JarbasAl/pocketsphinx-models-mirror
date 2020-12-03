from mycroft_stt_plugin_pocketpshinx.recognizer import PocketSphinxRecognizer


# https://github.com/JarbasIberianLanguageResources/iberian-sphinx

def get_brazilian_model():
    hmm = "/home/user/iberian-sphinx/pt-br/hmm"
    lm = "/home/user/iberian-sphinx/pt-br/pt-br.lm.tar.gz"
    pho = "/home/user/iberian-sphinx/pt-br/pt-br.dict"
    return hmm, lm, pho


def get_catalan_model():
    hmm = "/home/user/iberian-sphinx/ca-es/acoustic-model"
    lm = "/home/user/iberian-sphinx/ca-es/language-model.lm.bin"
    pho = "/home/user/iberian-sphinx/ca-es/pronounciation-dictionary.dict"
    return hmm, lm, pho


def get_spanish_model():
    hmm = "/home/user/iberian-sphinx/es-es/hmm"
    lm = "/home/user/iberian-sphinx/es-es/es-20k.lm.gz"
    pho = "/home/user/iberian-sphinx/es-es/es.dict"
    return hmm, lm, pho


def get_mexican_model():
    hmm = "/home/user/iberian-sphinx/es-mx/581HCDCONT10000SPA"
    lm = "/home/user/iberian-sphinx/es-mx/581HCDCONT10000SPA.lm.bin"
    pho = "/home/user/iberian-sphinx/es-mx/581HCDCONT10000SPA.dic"
    return hmm, lm, pho


# more models
# https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/

hmm, lm, pho = PocketSphinxRecognizer.get_default_english_model()
ps = PocketSphinxRecognizer(hmm, lm, pho)
test_file_en = "/home/user/mycroft-stt-plugin-pocketsphinx/test.wav"
print(ps.recognize_wav(test_file_en))