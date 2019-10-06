var button = document.getElementById("submit-text")
button.addEventListener("click", function () {
    var textInput = document.getElementById("text-input-area").value
    summarize(textInput)

})
async function summarize(text) {
    res = await deepai.callStandardApi("summarization", {
      text: text
    });
    console.log(res)
    var p = document.getElementById("interpretation")
    p.innerHTML = res.output
  }