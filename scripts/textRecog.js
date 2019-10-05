function imageToText(url) {
  console.log("Hello")
  Tesseract.recognize(
    url,
    'eng',
    { logger: m => console.log(m) }
  ).then(({ data: { text } }) => {
    linearizeText(text);
  })
}

function linearizeText(text) {
  var p = document.getElementById("interpretation")
  p.innerHTML = text
}

function processText(test) {

}