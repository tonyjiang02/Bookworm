function imageToText(url){
    Tesseract.recognize(
        url,
        'eng',
        { logger: m => console.log(m) }
      ).then(({ data: { text } }) => {
        linearizeText(text);
    })
}

function linearizeText(text){

}