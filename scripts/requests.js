const url = "http://10.100.19.116:5000/summarize?text="

function sendTextToServer(text){
    axios({
        method: 'get',
        url: url+text,
    }).then(function(response) {
        console.log(response)
    })
}