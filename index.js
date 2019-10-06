const fileInput = document.getElementById("img-input")
fileInput.addEventListener('change', function(e){
  processImage(e.target.files);
  if (document.querySelector("body.empty"))
    document.querySelector("body.empty").classList.remove("empty");
  if (document.querySelector(".loading.hide"))
    document.querySelector(".loading.hide").classList.remove(".hide");
  if (!document.querySelector(".text-area.hide") && document.querySelector(".text-area"))
    document.querySelector(".text-area").classList.add("hide");
})

function processImage(fileList) {
  let file = null;
  var url;
  for (let i =0; i<fileList.length; i++){
    if (fileList[i].type.match(/^image\//)) {
        file = fileList[i];
        break
    }
  }
  if (file !=null) {
    url = URL.createObjectURL(file);
    var imgpreview = document.querySelector(".img-preview > img");
    imgpreview.setAttribute('src', url);
    imageToText(url)
  }
}
// Register service worker to control making site work offline
if('serviceWorker' in navigator) {
  navigator.serviceWorker
           .register('/pwa-examples/a2hs/sw.js')
           .then(function() { console.log('Service Worker Registered'); });
}
window.addEventListener('beforeinstallprompt', (e) => {
  // Prevent Chrome 67 and earlier from automatically showing the prompt
  e.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = e;
  // Update UI to notify the user they can add to home screen
  addBtn.style.display = 'block';

  addBtn.addEventListener('click', (e) => {
    // hide our user interface that shows our A2HS button
    addBtn.style.display = 'none';
    // Show the prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the A2HS prompt');
        } else {
          console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
      });
  });
});
