from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from better_profanity import profanity
from fastapi.encoders import jsonable_encoder

class Book(BaseModel):
    text1: str

app = FastAPI()

@app.post("/prof")
def create_book(book: Book):
    cdr=book.text1
    # print(cdr)
    profanity.load_censor_words_from_file('C:\S\Projects and researches\Doions Project\Projects-Python\profanity api\wordlist.txt')
    text = cdr
    censored_text = profanity.censor(text)
    print(censored_text)
    # return(censored_text)

    if '****' in censored_text:
        res=1

    else:
        res=0


    if res==1:
        df=("This is violating our content Policy \n Please review your Question")

    else:
        df=("shifts to rest logic")

    result = {
        'state': res,
        'text': censored_text,
        'org':text
    }

    print(type(result))

    resu=jsonable_encoder(result)
    return JSONResponse(content=resu)


uvicorn.run(app, port=8000, host="127.0.0.1")



