def text_preprocess( text ) :
    try :
        text.encode('utf-8').decode('utf-8')
# convert to utf-8
        text = text.strip()
# string trim
        for chr in text :
            if ( not chr.isascii() ) :
                text = text.replace(chr, '')
# remove non ascii
        return text
    except :
        return None

# playground
while (1) :
    text = input()
    print(text_preprocess(text))