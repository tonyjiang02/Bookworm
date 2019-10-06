var button = getElementBydId("submit-button")
var url = ""
button.addEventListener("click", function() {
    var t1 = document.getElementById("mytextarea").value
    var t3 = document.getElementById("mytextvalue").value
    axios.post(url, {
        text: t1,
        subject:t3
    }).then(function(response) {
        console.log(response);
        document.getElementById("interpretation").innerHTML = response.summary;
    })
})