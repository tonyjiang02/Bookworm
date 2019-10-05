const url = "http://10.100.19.116:5000/summarize?text=asdfasdfasdfasdfasdfasdf"

function sendTextToServer(text){
    const data = {
        text: text
    }
    axios({
        method: 'get',
        url: url,
    }).then(data =>console.log(data)).catch(err=>console.log(err))
}