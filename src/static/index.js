document.addEventListener("DOMContentLoaded", function() {
    console.log("Hello world")
    //get the form, listen for when user submits
    document.getElementById("UrlForm").addEventListener("submit", function(event) {
        event.preventDefault();
        const urlInput = document.getElementById("Url").value.trim();

        if (urlInput != "") {
            fetch(`/api/v1/encode?url=${urlInput}`)
            .then(response => response.text())
            .then(data => {
                console.log(data);
                display = document.getElementById("shortenedUrl").innerText = data

                navigator.clipboard.writeText(data).then(() => {
                    alert("Text URL to clipboard!");
                });
            })
        }
    })
});
