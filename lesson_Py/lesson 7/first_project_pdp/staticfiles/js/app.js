let url = "http://127.0.0.1:8000/api/category/"
"get information from the above url via fetch and output it to the console"

function getCategory() {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
}